import os
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import aiohttp
import requests
from eth_typing import ChecksumAddress

from .. import EthereumNetwork
from .contract_metadata import ContractMetadata


class BlockscoutClientException(Exception):
    pass


class BlockScoutConfigurationProblem(BlockscoutClientException):
    pass


class BlockscoutClient:
    NETWORK_WITH_URL = {
        EthereumNetwork.GNOSIS: "https://gnosis.blockscout.com/api/v1/graphql",
        EthereumNetwork.ENERGY_WEB_CHAIN: "https://explorer.energyweb.org/graphiql",
        EthereumNetwork.ENERGY_WEB_VOLTA_TESTNET: "https://volta-explorer.energyweb.org/graphiql",
        EthereumNetwork.POLIS_MAINNET: "https://explorer.polis.tech/graphiql",
        EthereumNetwork.BOBA_NETWORK: "https://blockexplorer.boba.network/graphiql",
        EthereumNetwork.GATHER_DEVNET_NETWORK: "https://devnet-explorer.gather.network/graphiql",
        EthereumNetwork.GATHER_TESTNET_NETWORK: "https://testnet-explorer.gather.network/graphiql",
        EthereumNetwork.GATHER_MAINNET_NETWORK: "https://explorer.gather.network/graphiql",
        EthereumNetwork.METIS_GOERLI_TESTNET: "https://goerli.explorer.metisdevops.link/graphiql",
        EthereumNetwork.METIS_ANDROMEDA_MAINNET: "https://andromeda-explorer.metis.io/graphiql",
        EthereumNetwork.FUSE_MAINNET: "https://explorer.fuse.io/graphiql",
        EthereumNetwork.VELAS_EVM_MAINNET: "https://evmexplorer.velas.com/graphiql",
        EthereumNetwork.REI_NETWORK: "https://scan.rei.network/graphiql",
        EthereumNetwork.REI_CHAIN_TESTNET: "https://scan-test.rei.network/graphiql",
        EthereumNetwork.METER_MAINNET: "https://scan.meter.io/graphiql",
        EthereumNetwork.METER_TESTNET: "https://scan-warringstakes.meter.io/graphiql",
        EthereumNetwork.GODWOKEN_MAINNET: "https://v1.gwscan.com/graphiql",
        EthereumNetwork.VENIDIUM_TESTNET: "https://evm-testnet.venidiumexplorer.com/graphiql",
        EthereumNetwork.VENIDIUM_MAINNET: "https://evm.venidiumexplorer.com/graphiql",
        EthereumNetwork.KAIA_MAINNET: "https://scope.klaytn.com/graphiql",
        EthereumNetwork.ACALA_NETWORK: "https://blockscout.acala.network/graphiql",
        EthereumNetwork.KARURA_NETWORK_TESTNET: "https://blockscout.karura.network/graphiql",
        EthereumNetwork.ASTAR: "https://blockscout.com/astar/graphiql",
        EthereumNetwork.SHIDEN: "https://blockscout.com/shiden/graphiql",
        EthereumNetwork.EVMOS: "https://evm.evmos.org/graphiql",
        EthereumNetwork.EVMOS_TESTNET: "https://evm.evmos.dev/graphiql",
        EthereumNetwork.KCC_MAINNET: "https://scan.kcc.io/graphiql",
        EthereumNetwork.KCC_TESTNET: "https://scan-testnet.kcc.network/graphiql",
        EthereumNetwork.CROSSBELL: "https://scan.crossbell.io/graphiql",
        EthereumNetwork.ETHEREUM_CLASSIC: "https://blockscout.com/etc/mainnet/graphiql",
        EthereumNetwork.MORDOR_TESTNET: "https://blockscout.com/etc/mordor/graphiql",
        EthereumNetwork.SCROLL_SEPOLIA_TESTNET: "https://sepolia-blockscout.scroll.io/graphiql",
        EthereumNetwork.MANTLE: "https://explorer.mantle.xyz/api/v1/graphql",
        EthereumNetwork.MANTLE_TESTNET: "https://explorer.testnet.mantle.xyz/graphiql",
        EthereumNetwork.JAPAN_OPEN_CHAIN_MAINNET: "https://mainnet.japanopenchain.org/graphiql",
        EthereumNetwork.JAPAN_OPEN_CHAIN_TESTNET: "https://explorer.testnet.japanopenchain.org/graphiql",
        EthereumNetwork.ZETACHAIN_TESTNET: "https://zetachain-athens-3.blockscout.com/graphiql",
        EthereumNetwork.SCROLL: "https://blockscout.scroll.io/graphiql",
        EthereumNetwork.ROOTSTOCK_MAINNET: "https://rootstock.blockscout.com/graphiql",
        EthereumNetwork.ROOTSTOCK_TESTNET: "https://rootstock-testnet.blockscout.com/graphiql",
        EthereumNetwork.LINEA: "https://explorer.linea.build/graphiql",
        EthereumNetwork.LINEA_GOERLI: "https://explorer.goerli.linea.build/graphiql",
        EthereumNetwork.NEON_EVM_MAINNET: "https://neon.blockscout.com/graphiql",
        EthereumNetwork.NEON_EVM_DEVNET: "https://neon-devnet.blockscout.com/graphiql",
        EthereumNetwork.OASIS_SAPPHIRE: "https://explorer.sapphire.oasis.io/graphiql",
        EthereumNetwork.OASIS_SAPPHIRE_TESTNET: "https://testnet.explorer.sapphire.oasis.dev/graphiql",
        EthereumNetwork.CASCADIA_TESTNET: "https://explorer.cascadia.foundation/graphiql",
        EthereumNetwork.TENET: "https://tenetscan.io/graphiql",
        EthereumNetwork.TENET_TESTNET: "https://testnet.tenetscan.io/graphiql",
        EthereumNetwork.CRONOS_MAINNET: "https://cronos.org/explorer/graphiql",
        EthereumNetwork.CRONOS_TESTNET: "https://cronos.org/explorer/testnet3/graphiql",
        EthereumNetwork.THUNDERCORE_MAINNET: "https://explorer-mainnet.thundercore.com/graphiql",
        EthereumNetwork.THUNDERCORE_TESTNET: "https://explorer-testnet.thundercore.com/graphiql",
        EthereumNetwork.PGN_PUBLIC_GOODS_NETWORK: "https://explorer.publicgoods.network/graphiql",
        EthereumNetwork.SEPOLIA_PGN_PUBLIC_GOODS_NETWORK: "https://explorer.sepolia.publicgoods.network/graphiql",
        EthereumNetwork.ARTHERA_MAINNET: "https://explorer.arthera.net/graphiql",
        EthereumNetwork.ARTHERA_TESTNET: "https://explorer-test.arthera.net/graphiql",
        EthereumNetwork.MANTA_PACIFIC_MAINNET: "https://pacific-explorer.manta.network/graphiql",
        EthereumNetwork.KROMA: "https://blockscout.kroma.network/graphiql",
        EthereumNetwork.KROMA_SEPOLIA: "https://blockscout.sepolia.kroma.network/graphiql",
        EthereumNetwork.ZORA: "https://explorer.zora.energy/graphiql",
        EthereumNetwork.ZORA_SEPOLIA_TESTNET: "https://sepolia.explorer.zora.energy/graphiql",
        EthereumNetwork.HAQQ_NETWORK: "https://explorer.haqq.network/graphiql",
        EthereumNetwork.HAQQ_CHAIN_TESTNET: "https://explorer.testedge2.haqq.network/graphiql",
        EthereumNetwork.MODE: "https://explorer.mode.network/graphiql",
        EthereumNetwork.MODE_TESTNET: "https://sepolia.explorer.mode.network/graphiql",
        EthereumNetwork.MANTLE_SEPOLIA_TESTNET: "https://explorer.sepolia.mantle.xyz/api/v1/graphql",
        EthereumNetwork.OP_SEPOLIA_TESTNET: "https://optimism-sepolia.blockscout.com/graphiql",
        EthereumNetwork.UNREAL_OLD: "https://unreal.blockscout.com/graphiql",
        EthereumNetwork.TAIKO_KATLA_L2: "https://explorer.katla.taiko.xyz/graphiql",
        EthereumNetwork.SEI_DEVNET: "https://seitrace.com/graphiql",
        EthereumNetwork.LISK_SEPOLIA_TESTNET: "https://sepolia-blockscout.lisk.com/api/v1/graphql",
        EthereumNetwork.BOTANIX_TESTNET: "https://blockscout.botanixlabs.dev/graphiql",
        EthereumNetwork.REYA_NETWORK: "https://explorer.reya.network/graphiql",
        EthereumNetwork.AURORIA_TESTNET: "https://auroria.explorer.stratisevm.com/graphiql",
        EthereumNetwork.STRATIS_MAINNET: "https://explorer.stratisevm.com/graphiql",
        EthereumNetwork.SHIMMEREVM: "https://explorer.evm.shimmer.network/graphiql",
        EthereumNetwork.IOTA_EVM: "https://iota-evm.blockscout.com/graphiql",
        EthereumNetwork.BITROCK_MAINNET: "https://explorer.bit-rock.io/api/v1/graphql",
        EthereumNetwork.BITROCK_TESTNET: "https://testnetscan.bit-rock.io/api/v1/graphql",
        EthereumNetwork.OP_CELESTIA_RASPBERRY: "https://opcelestia-raspberry.gelatoscout.com/api/v1/graphql",
        EthereumNetwork.POLYGON_BLACKBERRY: "https://polygon-blackberry.gelatoscout.com/api/v1/graphql",
        EthereumNetwork.ARBITRUM_BLUEBERRY: "https://arb-blueberry.gelatoscout.com/api/v1/graphql",
        EthereumNetwork.RSS3_VSL_SEPOLIA_TESTNET: "https://scan.testnet.rss3.io/api/v1/graphql",
        EthereumNetwork.RSS3_VSL_MAINNET: "https://scan.rss3.io/api/v1/graphql",
        EthereumNetwork.CROSSFI: "https://scan.xfi.ms/graphiql",
        EthereumNetwork.CROSSFI_TESTNET: "https://scan.testnet.ms/graphiql",
        EthereumNetwork.ASTAR_ZKYOTO: "https://astar-zkyoto.blockscout.com/api/v1/graphql",
        EthereumNetwork.SAAKURU_MAINNET: "https://explorer.saakuru.network/graphiql",
        EthereumNetwork.REDSTONE: "https://explorer.redstone.xyz/api/v1/graphql",
        EthereumNetwork.GARNET_HOLESKY: "https://api.explorer.garnet.qry.live/api/v1/graphql",
        EthereumNetwork.TAIKO_HEKLA_L2: "https://blockscoutapi.hekla.taiko.xyz/graphiql",
        EthereumNetwork.ASTAR_ZKEVM: "https://astar-zkevm.explorer.startale.com/api/v1/graphql",
        EthereumNetwork.RE_AL: "https://explorer.re.al/api/v1/graphql",
        EthereumNetwork.UNREAL: "https://unreal.blockscout.com/api/v1/graphql",
        EthereumNetwork.LISK: "https://blockscout.lisk.com/api/v1/graphql",
        EthereumNetwork.OPEN_CAMPUS_CODEX: "https://opencampus-codex.blockscout.com/api/v1/graphql",
        EthereumNetwork.LORENZO: "https://scan.lorenzo-protocol.xyz/api/v1/graphql",
        EthereumNetwork.DODOCHAIN_TESTNET: "https://testnet-scan.dodochain.com/api/v1/graphql",
        EthereumNetwork.ETHERLINK_MAINNET: "https://explorer.etherlink.com/api/v1/graphql",
        EthereumNetwork.ETHERLINK_TESTNET: "https://testnet-explorer.etherlink.com/api/v1/graphql",
        EthereumNetwork.FLARE_MAINNET: "https://flare-explorer.flare.network/graphiql",
        EthereumNetwork.GNOSIS_CHIADO_TESTNET: "https://gnosis-chiado.blockscout.com/api/v1/graphql",
        EthereumNetwork.SONGBIRD_CANARY_NETWORK: "https://songbird-explorer.flare.network/graphiql",
        EthereumNetwork.SONGBIRD_TESTNET_COSTON: "https://coston-explorer.flare.network/graphiql",
        EthereumNetwork.FLARE_TESTNET_COSTON2: "https://coston2-explorer.flare.network/graphiql",
        EthereumNetwork.NAL_SEPOLIA_TESTNET: "https://testnet-scan.nal.network/api/v1/graphql",
        EthereumNetwork.ALEPH_ZERO_EVM: "https://evm-explorer.alephzero.org/api/v1/graphql",
        EthereumNetwork.SKOPJE_TESTNET: "https://skopje-explorer.gptprotocol.io/api/v1/graphql",
        EthereumNetwork.GPT_MAINNET: "https://explorer.gptprotocol.io/api/v1/graphql",
        EthereumNetwork.BOB_SEPOLIA: "https://bob-sepolia.explorer.gobob.xyz/api/v1/graphql",
        EthereumNetwork.SNAXCHAIN: "https://explorer.snaxchain.io/api/v1/graphql",
        EthereumNetwork.CITREA_TESTNET: "https://explorer.testnet.citrea.xyz/api/v1/graphql",
        EthereumNetwork.EDU: "https://educhain.blockscout.com/api/v1/graphql",
        EthereumNetwork.KAKAROT: "https://sepolia.kakarotscan.org/api/v1/graphql",
        EthereumNetwork.FILECOIN_MAINNET: "https://filecoin.blockscout.com/api/v1/graphql",
        EthereumNetwork.FILECOIN_CALIBRATION_TESTNET: "https://filecoin-testnet.blockscout.com/api/v1/graphql",
        EthereumNetwork.ABSTRACT: "https://explorer.mainnet.abs.xyz/api/v1/graphql",
        EthereumNetwork.ABSTRACT_SEPOLIA: "https://explorer.testnet.abs.xyz/api/v1/graphql",
        EthereumNetwork.AUTONOMYS_TAURUS_TESNET: "https://blockscout.taurus.autonomys.xyz/api/v1/graphql",
        EthereumNetwork.BERACHAIN:"test.blockscout.berachain.io",
        EthereumNetwork.GAME7_TESTNET: "https://testnet.game7.io/api/v1/graphql",
        EthereumNetwork.GAME7: "https://mainnet.game7.io/api/v1/graphql",
        EthereumNetwork.STORY_AENEID: "https://aeneid.storyscan.xyz/api/v1/graphql",
        EthereumNetwork.ACALA_NETWORK: "https://blockscout.acala.network/api/v2/",
        EthereumNetwork.ALEPH_ZERO_EVM: "https://evm-explorer.alephzero.org/api/v2/",
        EthereumNetwork.ARBITRUM_BLUEBERRY: "https://arb-blueberry.gelatoscout.com/api/v2/",
        EthereumNetwork.ARTHERA_MAINNET: "https://explorer.arthera.net/api/v2/",
        EthereumNetwork.ARTHERA_TESTNET: "https://explorer-test.arthera.net/api/v2/",
        EthereumNetwork.ASTAR_ZKEVM: "https://astar-zkevm.explorer.startale.com/api/v2/",
        EthereumNetwork.AURORIA_TESTNET: "https://auroria.explorer.stratisevm.com/api/v2/",
        EthereumNetwork.BAHAMUT: "https://api.ftnscan.com/api/v2/",
        EthereumNetwork.BOB_SEPOLIA: "https://bob-sepolia.explorer.gobob.xyz/api/v2/",
        EthereumNetwork.BITROCK_TESTNET: "https://testnetscan.bit-rock.io/api/v2/",
        EthereumNetwork.CONNEXT_SEPOLIA: "https://scan.testnet.everclear.org/api/v2/",
        EthereumNetwork.DODOCHAIN_TESTNET: "https://testnet-scan.dodochain.com/api/v2/",
        EthereumNetwork.EVERCLEAR_MAINNET: "https://scan.everclear.org/api/v2/",
        EthereumNetwork.EVMOS: "https://evm.evmos.org/api/v2/",
        EthereumNetwork.ETHERLINK_MAINNET: "https://explorer.etherlink.com/api/v2/",
        EthereumNetwork.EXSAT_MAINNET: "https://scan.exsat.network/api/v2/",
        EthereumNetwork.EXSAT_TESTNET: "https://scan-testnet.exsat.network/api/v2/",
        EthereumNetwork.FLARE_MAINNET: "https://flare-explorer.flare.network/api/v2/",
        EthereumNetwork.FLARE_TESTNET_COSTON2: "https://coston2-explorer.flare.network/api/v2/",
        EthereumNetwork.GAME7: "https://mainnet.game7.io/api/v2/",
        EthereumNetwork.GAME7_TESTNET: "https://testnet.game7.io/api/v2/",
        EthereumNetwork.GNOSIS: "https://gnosis.blockscout.com/api/v2/",
        EthereumNetwork.GNOSIS_CHIADO_TESTNET: "https://gnosis-chiado.blockscout.com/api/v2/",
        EthereumNetwork.GPT_MAINNET: "https://explorer.gptprotocol.io/api/v2/",
        EthereumNetwork.HAQQ_CHAIN_TESTNET: "https://explorer.testedge2.haqq.network/api/v2/",
        EthereumNetwork.HAQQ_NETWORK: "https://explorer.haqq.network/api/v2/",
        EthereumNetwork.HASHKEY_CHAIN: "https://explorer.hsk.xyz/api/v2/",
        EthereumNetwork.HASHKEY_CHAIN_TESTNET: "https://hashkeychain-testnet-explorer.alt.technology/api/v2/",
        EthereumNetwork.IOTA_EVM: "https://iota-evm.blockscout.com/api/v2/",
        EthereumNetwork.INK_SEPOLIA: "https://explorer-sepolia.inkonchain.com/api/v2/",
        EthereumNetwork.JAPAN_OPEN_CHAIN_MAINNET: "https://mainnet.japanopenchain.org/api/v2/",
        EthereumNetwork.JAPAN_OPEN_CHAIN_TESTNET: "https://explorer.testnet.japanopenchain.org/api/v2/",
        EthereumNetwork.KAIA_KAIROS_TESTNET: "https://baobab.scope.klaytn.com/api/v2/",
        EthereumNetwork.KAIA_MAINNET: "https://scope.klaytn.com/api/v2/",
        EthereumNetwork.KROMA: "https://blockscout.kroma.network/api/v2/",
        EthereumNetwork.KROMA_SEPOLIA: "https://blockscout.sepolia.kroma.network/api/v2/",
        EthereumNetwork.LINEA: "https://api-explorer.linea.build/api/v2/",
        EthereumNetwork.LISK: "https://blockscout.lisk.com/api/v2/",
        EthereumNetwork.LISK_SEPOLIA_TESTNET: "https://sepolia-blockscout.lisk.com/api/v2/",
        EthereumNetwork.LORENZO: "https://scan.lorenzo-protocol.xyz/api/v2/",
        EthereumNetwork.MANTLE: "https://explorer.mantle.xyz/api/v2/",
        EthereumNetwork.MANTLE_SEPOLIA_TESTNET: "https://explorer.sepolia.mantle.xyz/api/v2/",
        EthereumNetwork.MANTLE_TESTNET: "https://explorer.testnet.mantle.xyz/api/v2/",
        EthereumNetwork.MANTLE_TESTNET: "https://explorer.testnet.mantle.xyz/api/v2/",
        EthereumNetwork.MANTA_PACIFIC_MAINNET: "https://pacific-explorer.manta.network/api/v2/",
        EthereumNetwork.METER_MAINNET: "https://scan.meter.io/api/v2/",
        EthereumNetwork.METER_TESTNET: "https://scan-warringstakes.meter.io/api/v2/",
        EthereumNetwork.MODE: "https://explorer.mode.network/api/v2/",
        EthereumNetwork.MODE_TESTNET: "https://sepolia.explorer.mode.network/api/v2/",
        EthereumNetwork.NAL_SEPOLIA_TESTNET: "https://testnet-scan.nal.network/api/v2/",
        EthereumNetwork.NEON_EVM_DEVNET: "https://neon-devnet.blockscout.com/api/v2/",
        EthereumNetwork.NEON_EVM_MAINNET: "https://neon.blockscout.com/api/v2/",
        EthereumNetwork.OP_CELESTIA_RASPBERRY: "https://opcelestia-raspberry.gelatoscout.com/api/v2/",
        EthereumNetwork.OP_SEPOLIA_TESTNET: "https://optimism-sepolia.blockscout.com/api/v2/",
        EthereumNetwork.PLUME_DEVNET: "https://test-explorer.plumenetwork.xyz/api/v2/",
        EthereumNetwork.PLUME_MAINNET: "https://phoenix-explorer.plumenetwork.xyz/api/v2/",
        EthereumNetwork.Q_MAINNET: "https://explorer.q.org/api/v2/",
        EthereumNetwork.Q_TESTNET: "https://explorer.qtestnet.org/api/v2/",
        EthereumNetwork.REDSTONE: "https://explorer.redstone.xyz/api/v2/",
        EthereumNetwork.RE_AL: "https://explorer.re.al/api/v2/",
        EthereumNetwork.REYA_NETWORK: "https://explorer.reya.network/api/v2/",
        EthereumNetwork.ROOTSTOCK_MAINNET: "https://rootstock.blockscout.com/api/v2/",
        EthereumNetwork.ROOTSTOCK_TESTNET: "https://rootstock-testnet.blockscout.com/api/v2/",
        EthereumNetwork.SAAKURU_MAINNET: "https://explorer.saakuru.network/api/v2/",
        EthereumNetwork.SNAXCHAIN: "https://explorer.snaxchain.io/api/v2/",
        EthereumNetwork.SONGBIRD_CANARY_NETWORK: "https://songbird-explorer.flare.network/api/v2/",
        EthereumNetwork.SONGBIRD_TESTNET_COSTON: "https://coston-explorer.flare.network/api/v2/",
        EthereumNetwork.STORY_ODYSSEY_TESTNET: "https://odyssey-testnet-explorer.storyscan.xyz/api/v2/",
        EthereumNetwork.SWELLCHAIN: "https://explorer.swellnetwork.io/api/v2/",
        EthereumNetwork.SWELLCHAIN_TESTNET: "https://swell-testnet-explorer.alt.technology/api/v2/",
        EthereumNetwork.TAIKO_HEKLA_L2: "https://blockscoutapi.hekla.taiko.xyz/api/v2/",
        EthereumNetwork.VANA_MOKSHA_TESTNET: "https://api.moksha.vanascan.io/api/v2/",
        EthereumNetwork.ZETACHAIN_TESTNET: "https://zetachain-athens-3.blockscout.com/api/v2/",
        EthereumNetwork.ZORA: "https://explorer.zora.energy/api/v2/",
        EthereumNetwork.ZORA_SEPOLIA_TESTNET: "https://sepolia.explorer.zora.energy/api/v2/",
        EthereumNetwork.EVM_ON_FLOW: "https://evm.flowscan.io/api/v2",
        EthereumNetwork.EVM_ON_FLOW_TESTNET: "https://evm-testnet.flowscan.io/api/v2",
        EthereumNetwork.BIRDLAYER: "https://scan.birdlayer.xyz/api/v2",
        EthereumNetwork.EXPCHAIN_TESTNET: "https://blockscout-testnet.expchain.ai/api/v2",
    }

    def __init__(
        self,
        network: EthereumNetwork,
        request_timeout: int = int(
            os.environ.get("BLOCKSCOUT_CLIENT_REQUEST_TIMEOUT", 10)
        ),
    ):
        self.network = network
        self.api_url = self.NETWORK_WITH_URL.get(network, "")
        self.request_timeout = request_timeout
        if not self.api_url:
            raise BlockScoutConfigurationProblem(
                f"Network {network.name} - {network.value} not supported"
            )
        self.http_session = requests.Session()

    def build_url(self, path: str):
        return urljoin(self.api_url, path)

    def _do_request(self, url: str) -> Optional[Dict[str, Any]]:
        response = self.http_session.get(url, timeout=10)
        if not response.ok:
            return None

        return response.json()

    @staticmethod
    def _process_contract_metadata(
        contract_data: dict[str, Any]
    ) -> Optional[ContractMetadata]:
        """
        Return a ContractMetadata from BlockScout response

        :param contract_data:
        :return:
        """
        if abi := contract_data.get("abi"):
            name = contract_data["name"]
            implementations: list = contract_data.get("implementations", [])
            return ContractMetadata(
                name,
                abi,
                False,
                implementations[0]["address"] if implementations else None,
            )
        return None

    def get_contract_metadata(
        self, address: ChecksumAddress
    ) -> Optional[ContractMetadata]:
        contract_request = self.build_url(f"smart-contracts/{address}")
        contract_data = self._do_request(contract_request)
        if contract_data:
            return self._process_contract_metadata(contract_data)
        return None


class AsyncBlockscoutClient(BlockscoutClient):
    def __init__(
        self,
        network: EthereumNetwork,
        request_timeout: int = int(
            os.environ.get("BLOCKSCOUT_CLIENT_REQUEST_TIMEOUT", 10)
        ),
        max_requests: int = int(os.environ.get("BLOCKSCOUT_CLIENT_MAX_REQUESTS", 100)),
    ):
        super().__init__(network, request_timeout)
        # Limit simultaneous connections to the same host.
        self.async_session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(limit_per_host=max_requests)
        )

    async def _async_do_request(self, url: str) -> Optional[Dict[str, Any]]:
        """
        Asynchronous version of _do_request
        """
        async with self.async_session.get(
            url, timeout=self.request_timeout
        ) as response:
            if not response.ok:
                return None

            return await response.json()

    async def async_get_contract_metadata(
        self, address: ChecksumAddress
    ) -> Optional[ContractMetadata]:
        contract_request = self.build_url(f"smart-contracts/{address}")
        contract_data = await self._async_do_request(contract_request)
        if contract_data:
            return self._process_contract_metadata(contract_data)
        return None
