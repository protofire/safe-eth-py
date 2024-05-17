import json
from typing import Any, Dict, Optional
from urllib.parse import urljoin

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
        EthereumNetwork.GODWOKEN_TESTNET_V1: "https://v1.betanet.gwscan.com/graphiql",
        EthereumNetwork.GODWOKEN_MAINNET: "https://v1.gwscan.com/graphiql",
        EthereumNetwork.VENIDIUM_TESTNET: "https://evm-testnet.venidiumexplorer.com/graphiql",
        EthereumNetwork.VENIDIUM_MAINNET: "https://evm.venidiumexplorer.com/graphiql",
        EthereumNetwork.KLAYTN_TESTNET_BAOBAB: "https://baobab.scope.klaytn.com/graphiql",
        EthereumNetwork.KLAYTN_MAINNET_CYPRESS: "https://scope.klaytn.com/graphiql",
        EthereumNetwork.ACALA_NETWORK: "https://blockscout.acala.network/graphiql",
        EthereumNetwork.KARURA_NETWORK_TESTNET: "https://blockscout.karura.network/graphiql",
        EthereumNetwork.ASTAR: "https://astar.blockscout.com/api/v1/graphql",
        EthereumNetwork.SHIDEN: "https://shiden.blockscout.com/api/v1/graphql",
        EthereumNetwork.EVMOS: "https://evm.evmos.org/graphiql",
        EthereumNetwork.EVMOS_TESTNET: "https://evm.evmos.dev/graphiql",
        EthereumNetwork.KCC_MAINNET: "https://scan.kcc.io/graphiql",
        EthereumNetwork.KCC_TESTNET: "https://scan-testnet.kcc.network/graphiql",
        EthereumNetwork.CROSSBELL: "https://scan.crossbell.io/graphiql",
        EthereumNetwork.ETHEREUM_CLASSIC: "https://blockscout.com/etc/mainnet/graphiql",
        EthereumNetwork.MORDOR_TESTNET: "https://blockscout.com/etc/mordor/graphiql",
        EthereumNetwork.MANTLE: "https://explorer.mantle.xyz/api/v1/graphql",
        EthereumNetwork.JAPAN_OPEN_CHAIN_MAINNET: "https://mainnet.japanopenchain.org/graphiql",
        EthereumNetwork.JAPAN_OPEN_CHAIN_TESTNET: "https://explorer.testnet.japanopenchain.org/graphiql",
        EthereumNetwork.ZETACHAIN_ATHENS_3_TESTNET: "https://zetachain-athens-3.blockscout.com/api/v1/graphql",
        EthereumNetwork.ROOTSTOCK_MAINNET: "https://rootstock.blockscout.com/api/v1/graphql",
        EthereumNetwork.ROOTSTOCK_TESTNET: "https://rootstock-testnet.blockscout.com/api/v1/graphql",
        EthereumNetwork.LINEA_SEPOLIA: "https://explorer.sepolia.linea.build/graphiql",
        EthereumNetwork.LINEA_TESTNET: "https://explorer.goerli.linea.build/graphiql",
        EthereumNetwork.NEON_EVM_MAINNET: "https://neon.blockscout.com/api/v1/graphql",
        EthereumNetwork.NEON_EVM_DEVNET: "https://neon-devnet.blockscout.com/api/v1/graphql",
        EthereumNetwork.TENET: "https://tenetscan.io/graphiql",
        EthereumNetwork.TENET_TESTNET: "https://testnet.tenetscan.io/api/v1/graphql",
        EthereumNetwork.CRONOS_MAINNET: "https://cronos.org/explorer/graphiql",
        EthereumNetwork.CRONOS_TESTNET: "https://cronos.org/explorer/testnet3/graphiql",
        EthereumNetwork.THUNDERCORE_MAINNET: "https://explorer-mainnet.thundercore.com/graphiql",
        EthereumNetwork.THUNDERCORE_TESTNET: "https://explorer-testnet.thundercore.com/graphiql",
        EthereumNetwork.PGN_PUBLIC_GOODS_NETWORK: "https://explorer.publicgoods.network/api/v1/graphql",
        EthereumNetwork.SEPOLIA_PGN_PUBLIC_GOODS_NETWORK: "https://explorer.sepolia.publicgoods.network/graphiql",
        EthereumNetwork.ARTHERA_MAINNET: "https://explorer.arthera.net/graphiql",
        EthereumNetwork.ARTHERA_TESTNET: "https://explorer-test.arthera.net/graphiql",
        EthereumNetwork.MANTA_PACIFIC_MAINNET: "https://pacific-explorer.manta.network/api/v1/graphql",
        EthereumNetwork.KROMA: "https://blockscout.kroma.network/api/v1/graphql",
        EthereumNetwork.KROMA_SEPOLIA: "https://blockscout.sepolia.kroma.network/api/v1/graphql",
        EthereumNetwork.ZORA: "https://explorer.zora.energy/api/v1/graphql",
        EthereumNetwork.ZORA_SEPOLIA_TESTNET: "https://sepolia.explorer.zora.energy/api/v1/graphql",
        EthereumNetwork.HAQQ_NETWORK: "https://explorer.haqq.network/graphiql",
        EthereumNetwork.HAQQ_CHAIN_TESTNET: "https://explorer.testedge2.haqq.network/graphiql",
        EthereumNetwork.MODE: "https://explorer.mode.network/api/v1/graphql",
        EthereumNetwork.MODE_TESTNET: "https://sepolia.explorer.mode.network/api/v1/graphql",
        EthereumNetwork.MANTLE_SEPOLIA_TESTNET: "https://explorer.sepolia.mantle.xyz/api/v1/graphql",
        EthereumNetwork.OP_SEPOLIA_TESTNET: "https://optimism-sepolia.blockscout.com/api/v1/graphql",
        EthereumNetwork.UNREAL_TESTNET: "https://unreal.blockscout.com/api/v1/graphql",
        EthereumNetwork.SEI_DEVNET: "https://seitrace.com/api/v1/graphql",
        EthereumNetwork.LISK_SEPOLIA_TESTNET: "https://sepolia-blockscout.lisk.com/api/v1/graphql",
        EthereumNetwork.ZETACHAIN_MAINNET: "https://zetachain.blockscout.com/api/v1/graphql",
        EthereumNetwork.IMMUTABLE_ZKEVM_TESTNET: "https://explorer.testnet.immutable.com/api/v1/graphql",
        EthereumNetwork.IMMUTABLE_ZKEVM: "https://explorer.immutable.com/api/v1/graphql",
        EthereumNetwork.REAL_MAINNET: "https://explorer.re.al/api/v1/graphql",
        EthereumNetwork.REYA_NETWORK: "https://explorer.reya.network/api/v1/graphql",
        EthereumNetwork.CROSSFI_TESTNET: "https://scan.testnet.ms/graphiql",
        EthereumNetwork.FRAXTAL_SEPOLIA: "https://explorer.testnet-sepolia.frax.com/api/v1/graphql",
        EthereumNetwork.BOB: "https://explorer.gobob.xyz/api/v1/graphql",
        EthereumNetwork.ETHERLITE_CHAIN: "https://testnet-explorer.gobob.xyz/api/v1/graphql",  # BOB Testnet
        EthereumNetwork.OP_CELESTIA_RASPBERRY: "https://opcelestia-raspberry.gelatoscout.com/api/v1/graphql",
        EthereumNetwork.ARBITRUM_BLUEBERRY: "https://arb-blueberry.gelatoscout.com/api/v1/graphql",
        EthereumNetwork.POLYGON_BLACKBERRY: "https://polygon-blackberry.gelatoscout.com/api/v1/graphql",
        EthereumNetwork.REDSTONE: "https://api.explorer.redstonechain.com/api/v1/graphql",
        EthereumNetwork.GARNET_HOLESKY: "https://api.explorer.garnet.qry.live/api/v1/graphql",
        EthereumNetwork.LISK: "https://blockscout.lisk.com/api/v1/graphql",
        EthereumNetwork.TAIKO_HEKLA_L2: "https://explorer.hekla.taiko.xyz/api/v1/graphql"
    }

    def __init__(self, network: EthereumNetwork):
        self.network = network
        self.grahpql_url = self.NETWORK_WITH_URL.get(network)
        if self.grahpql_url is None:
            raise BlockScoutConfigurationProblem(
                f"Network {network.name} - {network.value} not supported"
            )
        self.http_session = requests.Session()

    def build_url(self, path: str):
        return urljoin(self.grahpql_url, path)

    def _do_request(self, url: str, query: str) -> Optional[Dict[str, Any]]:
        response = self.http_session.post(url, json={"query": query}, timeout=10)
        if not response.ok:
            return None

        return response.json()

    def get_contract_metadata(
            self, address: ChecksumAddress
    ) -> Optional[ContractMetadata]:
        query = '{address(hash: "%s") { hash, smartContract {name, abi} }}' % address
        result = self._do_request(self.grahpql_url, query)
        if (
                result
                and "error" not in result
                and result.get("data", {}).get("address", {})
                and result["data"]["address"]["smartContract"]
        ):
            smart_contract = result["data"]["address"]["smartContract"]
            return ContractMetadata(
                smart_contract["name"], json.loads(smart_contract["abi"]), False
            )
