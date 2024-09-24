from enum import Enum, unique


class EthereumNetworkNotSupported(Exception):
    pass


@unique
class EthereumNetwork(Enum):
    """
    Use https://chainlist.org/ as a reference
    """

    UNKNOWN = -1
    OLYMPIC = 0
    MAINNET = 1
    EXPANSE_NETWORK = 2
    ROPSTEN = 3
    RINKEBY = 4
    GOERLI = 5
    KOTTI_TESTNET = 6
    THAICHAIN = 7
    UBIQ = 8
    UBIQ_NETWORK_TESTNET = 9
    OPTIMISM = 10
    METADIUM_MAINNET = 11
    METADIUM_TESTNET = 12
    DIODE_TESTNET_STAGING = 13
    FLARE_MAINNET = 14
    DIODE_PRENET = 15
    FLARE_TESTNET_COSTON = 16
    THAICHAIN_2_0_THAIFI = 17
    THUNDERCORE_TESTNET = 18
    SONGBIRD_CANARY_NETWORK = 19
    ELASTOS_SMART_CHAIN = 20
    ELASTOS_SMART_CHAIN_TESTNET = 21
    ELA_DID_SIDECHAIN_MAINNET = 22
    ELA_DID_SIDECHAIN_TESTNET = 23
    KARDIACHAIN_MAINNET = 24
    CRONOS_MAINNET = 25
    GENESIS_L1_TESTNET = 26
    SHIBACHAIN = 27
    BOBA_NETWORK_RINKEBY_TESTNET = 28
    GENESIS_L1 = 29
    ROOTSTOCK_MAINNET = 30
    ROOTSTOCK_TESTNET = 31
    GOODDATA_TESTNET = 32
    GOODDATA_MAINNET = 33
    SECURECHAIN_MAINNET = 34
    TBWG_CHAIN = 35
    DXCHAIN_MAINNET = 36
    XPLA_MAINNET = 37
    VALORBIT = 38
    U2U_SOLARIS_MAINNET = 39
    TELOS_EVM_MAINNET = 40
    TELOS_EVM_TESTNET = 41
    LUKSO_MAINNET = 42
    DARWINIA_PANGOLIN_TESTNET = 43
    CRAB_NETWORK = 44
    DARWINIA_PANGORO_TESTNET = 45
    DARWINIA_NETWORK = 46
    ACRIA_INTELLICHAIN = 47
    ENNOTHEM_MAINNET_PROTEROZOIC = 48
    ENNOTHEM_TESTNET_PIONEER = 49
    XDC_NETWORK = 50
    XDC_APOTHEM_NETWORK = 51
    COINEX_SMART_CHAIN_MAINNET = 52
    COINEX_SMART_CHAIN_TESTNET = 53
    OPENPIECE_MAINNET = 54
    ZYX_MAINNET = 55
    BNB_SMART_CHAIN_MAINNET = 56
    SYSCOIN_MAINNET = 57
    ONTOLOGY_MAINNET = 58
    EOS_EVM_LEGACY = 59
    GOCHAIN = 60
    ETHEREUM_CLASSIC = 61
    MORDEN_TESTNET = 62
    MORDOR_TESTNET = 63
    ELLAISM = 64
    OKEXCHAIN_TESTNET = 65
    OKXCHAIN_MAINNET = 66
    DBCHAIN_TESTNET = 67
    SOTERONE_MAINNET = 68
    OPTIMISM_KOVAN = 69
    HOO_SMART_CHAIN = 70
    CONFLUX_ESPACE_TESTNET = 71
    DXCHAIN_TESTNET = 72
    FNCY = 73
    IDCHAIN_MAINNET = 74
    DECIMAL_SMART_CHAIN_MAINNET = 75
    MIX = 76
    POA_NETWORK_SOKOL = 77
    PRIMUSCHAIN_MAINNET = 78
    ZENITH_MAINNET = 79
    GENECHAIN = 80
    JAPAN_OPEN_CHAIN_MAINNET = 81
    METER_MAINNET = 82
    METER_TESTNET = 83
    LINQTO_DEVNET = 84
    GATECHAIN_TESTNET = 85
    GATECHAIN_MAINNET = 86
    NOVA_NETWORK = 87
    TOMOCHAIN = 88
    TOMOCHAIN_TESTNET = 89
    GARIZON_STAGE0 = 90
    GARIZON_STAGE1 = 91
    GARIZON_STAGE2 = 92
    GARIZON_STAGE3 = 93
    SWISSDLT = 94
    CAMDL_MAINNET = 95
    BITKUB_CHAIN = 96
    BNB_SMART_CHAIN_TESTNET = 97
    SIX_PROTOCOL = 98
    POA_NETWORK_CORE = 99
    GNOSIS = 100
    ETHERINC = 101
    WEB3GAMES_TESTNET = 102
    WORLDLAND_MAINNET = 103
    KAIBA_LIGHTNING_CHAIN_TESTNET = 104
    WEB3GAMES_DEVNET = 105
    VELAS_EVM_MAINNET = 106
    NEBULA_TESTNET = 107
    THUNDERCORE_MAINNET = 108
    SHIBARIUM = 109
    PROTON_TESTNET = 110
    ETHERLITE_CHAIN = 111 # BOB Testnet
    COINBIT_MAINNET = 112
    DEHVO = 113
    FLARE_TESTNET_COSTON2 = 114
    DEBANK_TESTNET_DEPRECATED = 115
    DEBANK_MAINNET = 116
    UPTICK_MAINNET = 117
    ARCOLOGY_TESTNET = 118
    ENULS_MAINNET = 119
    ENULS_TESTNET = 120
    REALCHAIN_MAINNET = 121
    FUSE_MAINNET = 122
    FUSE_SPARKNET = 123
    DECENTRALIZED_WEB_MAINNET = 124
    OYCHAIN_TESTNET = 125
    OYCHAIN_MAINNET = 126
    FACTORY_127_MAINNET = 127
    HUOBI_ECO_CHAIN_MAINNET = 128
    PROTOJUMBO_TESTNET = 129
    ENGRAM_TESTNET = 131
    IEXEC_SIDECHAIN = 134
    ALYX_CHAIN_TESTNET = 135
    DEAMCHAIN_MAINNET = 136
    POLYGON = 137
    DEFI_ORACLE_META_MAINNET = 138
    WOOPCHAIN_MAINNET = 139
    OPENPIECE_TESTNET = 141
    DAX_CHAIN = 142
    PHI_NETWORK_V2 = 144
    SHIMMEREVM = 148
    SIX_PROTOCOL_TESTNET = 150
    REDBELLY_NETWORK_MAINNET = 151
    REDBELLY_NETWORK_DEVNET = 152
    REDBELLY_NETWORK_TESTNET = 153
    REDBELLY_NETWORK_TGE = 154
    TENET_TESTNET = 155
    OEBLOCK_TESTNET = 156
    ARMONIA_EVA_CHAIN_MAINNET = 160
    ARMONIA_EVA_CHAIN_TESTNET = 161
    LIGHTSTREAMS_TESTNET = 162
    LIGHTSTREAMS_MAINNET = 163
    OMNI_TESTNET = 165
    ATOSHI_TESTNET = 167
    AIOZ_NETWORK = 168
    MANTA_PACIFIC_MAINNET = 169
    HOO_SMART_CHAIN_TESTNET = 170
    LATAM_BLOCKCHAIN_RESIL_TESTNET = 172
    AME_CHAIN_MAINNET = 180
    MINT_MAINNET = 185
    SEELE_MAINNET = 186
    BMC_MAINNET = 188
    BMC_TESTNET = 189
    CRYPTO_EMERGENCY = 193
    X_LAYER_TESTNET = 195
    X_LAYER_MAINNET = 196
    NEUTRINOS_TESTNET = 197
    BITCHAIN_MAINNET = 198
    BITTORRENT_CHAIN_MAINNET = 199
    ARBITRUM_ON_XDAI = 200
    MOAC_TESTNET = 201
    OPBNB_MAINNET = 204
    VINUCHAIN_TESTNET = 206
    VINUCHAIN_NETWORK = 207
    STRUCTX_MAINNET = 208
    BITNET = 210
    FREIGHT_TRUST_NETWORK = 211
    MAP_MAKALU = 212
    SHINARIUM_MAINNET = 214
    SIRIUSNET_V2 = 217
    SOTERONE_MAINNET_OLD = 218
    SCALIND_TESTNET = 220
    PERMISSION = 222
    LACHAIN_MAINNET = 225
    LACHAIN_TESTNET = 226
    SWAPDEX = 230
    DEAMCHAIN_TESTNET = 236
    BLAST_MAINNET = 238
    PLINGA_MAINNET = 242
    ENERGY_WEB_CHAIN = 246
    OASYS_MAINNET = 248
    FANTOM_OPERA = 250
    FRAXTAL = 252
    KROMA = 255
    HUOBI_ECO_CHAIN_TESTNET = 256
    SETHEUM = 258
    NEONLINK_MAINNET = 259
    SUR_BLOCKCHAIN_NETWORK = 262
    HIGH_PERFORMANCE_BLOCKCHAIN = 269
    EGONCOIN_MAINNET = 271
    LACHAIN = 274
    ZKSYNC_ERA_GOERLI_TESTNET_DEPRECATED = 280
    BOBA_NETWORK = 288
    ORDERLY_MAINNET = 291
    HEDERA_MAINNET = 295
    HEDERA_TESTNET = 296
    HEDERA_PREVIEWNET = 297
    HEDERA_LOCALNET = 298
    ZKSYNC_SEPOLIA_TESTNET = 300
    BOBAOPERA = 301
    NEUROCHAIN_TESTNET = 303
    WYZTH_TESTNET = 309
    OMAX_MAINNET = 311
    NEUROCHAIN_MAINNET = 313
    FILECOIN_MAINNET = 314
    KCC_MAINNET = 321
    KCC_TESTNET = 322
    ZKSYNC_MAINNET = 324
    WEB3Q_MAINNET = 333
    DFK_CHAIN_TEST = 335
    SHIDEN = 336
    CRONOS_TESTNET = 338
    THETA_MAINNET = 361
    THETA_SAPPHIRE_TESTNET = 363
    THETA_AMBER_TESTNET = 364
    THETA_TESTNET = 365
    PULSECHAIN = 369
    CONSTA_TESTNET = 371
    LISINSKI = 385
    NATIV3_MAINNET = 399
    HYPERONCHAIN_TESTNET = 400
    OZONE_CHAIN_TESTNET = 401
    PEPE_CHAIN_MAINNET = 411
    SX_NETWORK_MAINNET = 416
    LATESTNET = 418
    OPTIMISM_GOERLI_TESTNET = 420
    PGN_PUBLIC_GOODS_NETWORK = 424
    ZEETH_CHAIN = 427
    GESO_VERSE = 428
    TEN_TESTNET = 443
    SYNAPSE_CHAIN_TESTNET = 444
    ARZIO_CHAIN = 456
    AREON_NETWORK_TESTNET = 462
    AREON_NETWORK_MAINNET = 463
    RUPAYA = 499
    CAMINO_C_CHAIN = 500
    COLUMBUS_TEST_NETWORK = 501
    DOUBLE_A_CHAIN_MAINNET = 512
    DOUBLE_A_CHAIN_TESTNET = 513
    GEAR_ZERO_NETWORK_MAINNET = 516
    XT_SMART_CHAIN_MAINNET = 520
    FIRECHAIN_MAINNET = 529
    F_XCORE_MAINNET_NETWORK = 530
    CANDLE = 534
    PAWCHAIN_TESTNET = 542
    VELA1_CHAIN_MAINNET = 555
    TAO_NETWORK = 558
    DOGECHAIN_TESTNET = 568
    ROLLUX_MAINNET = 570
    METACHAIN_MAINNET = 571
    METIS_STARDUST_TESTNET = 588
    ASTAR = 592
    ACALA_MANDALA_TESTNET_TC9 = 595
    KARURA_NETWORK_TESTNET = 596
    ACALA_NETWORK_TESTNET = 597
    METIS_GOERLI_TESTNET = 599
    MESHNYAN_TESTNET = 600
    VINE_TESTNET = 601
    GRAPHLINQ_BLOCKCHAIN_MAINNET = 614
    AVOCADO = 634
    SX_NETWORK_TESTNET = 647
    ENDURANCE_SMART_CHAIN_MAINNET = 648
    KALICHAIN_TESTNET = 653
    KALICHAIN = 654
    PIXIE_CHAIN_TESTNET = 666
    LAOS_ARRAKIS = 667
    JUNCACHAIN = 668
    JUNCACHAIN_TESTNET = 669
    KARURA_NETWORK = 686
    REDSTONE = 690
    STAR_SOCIAL_TESTNET = 700
    BLOCKCHAIN_STATION_MAINNET = 707
    BLOCKCHAIN_STATION_TESTNET = 708
    HIGHBURY = 710
    SHIBARIUM_BETA = 719
    LYCAN_CHAIN = 721
    BLUCRATES = 727
    CANTO_TESTNET = 740
    VENTION_SMART_CHAIN_TESTNET = 741
    SCRIPT_TESTNET = 742
    QL1 = 766
    OPENCHAIN_TESTNET = 776
    CHEAPETH = 777
    MAAL_CHAIN = 786
    ACALA_NETWORK = 787
    AEROCHAIN_TESTNET = 788
    PATEX = 789
    LUCID_BLOCKCHAIN = 800
    HAIC = 803
    PORTAL_FANTASY_CHAIN_TEST = 808
    HAVEN1_TESTNET = 810
    QITMEER = 813
    FIRECHAIN_ZKEVM = 814
    BEONE_CHAIN_MAINNET = 818
    CALLISTO_MAINNET = 820
    CALLISTO_TESTNET_DEPRECATED = 821
    TARAXA_MAINNET = 841
    TARAXA_TESTNET = 842
    ZEETH_CHAIN_DEV = 859
    FANTASIA_CHAIN_MAINNET = 868
    BANDAI_NAMCO_RESEARCH_VERSE_MAINNET = 876
    DEXIT_NETWORK = 877
    AMBROS_CHAIN_MAINNET = 880
    WANCHAIN = 888
    GARIZON_TESTNET_STAGE0 = 900
    GARIZON_TESTNET_STAGE1 = 901
    GARIZON_TESTNET_STAGE2 = 902
    GARIZON_TESTNET_STAGE3 = 903
    PORTAL_FANTASY_CHAIN = 909
    DECENTRABONE_LAYER1_TESTNET = 910
    RINIA_TESTNET = 917
    MODE_TESTNET = 919
    YIDARK_CHAIN_MAINNET = 927
    PULSECHAIN_TESTNET = 940
    PULSECHAIN_TESTNET_V2B = 941
    PULSECHAIN_TESTNET_V3 = 942
    PULSECHAIN_TESTNET_V4 = 943
    MUNODE_TESTNET = 956
    LYRA_CHAIN = 957
    BTC20_SMART_CHAIN = 963
    OORT_MAINNET = 970
    OORT_HUYGENS = 971
    OORT_ASCRAEUS = 972
    NEPAL_BLOCKCHAIN_NETWORK = 977
    TOP_MAINNET_EVM = 980
    MEMO_SMART_CHAIN_MAINNET = 985
    TOP_MAINNET = 989
    ELIBERTY_MAINNET = 990
    _5IRECHAIN_THUNDER = 997
    LUCKY_NETWORK = 998
    WANCHAIN_TESTNET = 999
    GTON_MAINNET = 1000
    KLAYTN_TESTNET_BAOBAB = 1001
    TECTUM_EMISSION_TOKEN = 1003
    T_EKTA = 1004
    NEWTON_TESTNET = 1007
    EURUS_MAINNET = 1008
    EVRICE_NETWORK = 1010
    NEWTON = 1012
    SAKURA = 1022
    CLOVER_TESTNET = 1023
    CLV_PARACHAIN = 1024
    BITTORRENT_CHAIN_TESTNET = 1028
    CONFLUX_ESPACE = 1030
    PROXY_NETWORK_TESTNET = 1031
    BRONOS_TESTNET = 1038
    BRONOS_MAINNET = 1039
    SHIMMEREVM_TESTNET_DEPRECATED = 1071
    SHIMMEREVM_TESTNET_DEPRECATED_1072 = 1072
    SHIMMEREVM_TESTNET = 1073
    MINTARA_TESTNET = 1079
    MINTARA_MAINNET = 1080
    METIS_ANDROMEDA_MAINNET = 1088
    HUMANS_AI_MAINNET = 1089
    MOAC_MAINNET = 1099
    POLYGON_ZKEVM = 1101
    BLXQ_TESTNET = 1107
    BLXQ_MAINNET = 1108
    WEMIX3_0_MAINNET = 1111
    WEMIX3_0_TESTNET = 1112
    CORE_BLOCKCHAIN_TESTNET = 1115
    CORE_BLOCKCHAIN_MAINNET = 1116
    DOGCOIN_MAINNET = 1117
    DEFICHAIN_EVM_NETWORK_MAINNET = 1130
    DEFICHAIN_EVM_NETWORK_TESTNET = 1131
    DEFIMETACHAIN_CHANGI_TESTNET = 1133
    LISK = 1135
    AMSTAR_TESTNET = 1138
    MATHCHAIN = 1139
    MATHCHAIN_TESTNET = 1140
    SYMPLEXIA_SMART_CHAIN = 1149
    ORIGIN_TESTNET = 1170
    SMART_HOST_TEKNOLOJI_TESTNET = 1177
    IORA_CHAIN = 1197
    EVANESCO_TESTNET = 1201
    WORLD_TRADE_TECHNICAL_CHAIN_MAINNET = 1202
    POPCATEUM_MAINNET = 1213
    ENTERCHAIN_MAINNET = 1214
    EXZO_NETWORK_MAINNET = 1229
    ULTRON_TESTNET = 1230
    ULTRON_MAINNET = 1231
    STEP_NETWORK = 1234
    ARC_MAINNET = 1243
    ARC_TESTNET = 1244
    OM_PLATFORM_MAINNET = 1246
    DOGETHER_MAINNET = 1248
    CIC_CHAIN_TESTNET = 1252
    HALO_MAINNET = 1280
    MOONBEAM = 1284
    MOONRIVER = 1285
    MOONROCK_OLD = 1286
    MOONBASE_ALPHA = 1287
    MOONROCK = 1288
    SWISSTRONIK_TESTNET = 1291
    BOBABEAM = 1294
    BOBABASE_TESTNET = 1297
    DOS_FUJI_SUBNET = 1311
    ALYX_MAINNET = 1314
    AIA_MAINNET = 1319
    AIA_TESTNET = 1320
    SEI_NETWORK = 1329
    GANACHE = 1337
    ELYSIUM_TESTNET = 1338
    ELYSIUM_MAINNET = 1339
    BLITZ_SUBNET = 1343
    CIC_CHAIN_MAINNET = 1353
    ZAFIRIUM_MAINNET = 1369
    KALAR_CHAIN = 1379
    AMSTAR_MAINNET = 1388
    JOSEON_MAINNET = 1392
    POLYGON_ZKEVM_TESTNET_OLD = 1402
    POLYGON_ZKEVM_TESTNET_PRE_AUDIT_UPGRADED = 1422
    RIKEZA_NETWORK_MAINNET = 1433
    LIVING_ASSETS_MAINNET = 1440
    POLYGON_ZKEVM_TESTNET = 1442
    GIL_TESTNET = 1452
    CTEX_SCAN_BLOCKCHAIN = 1455
    BEVM_CANARY = 1501
    SHERPAX_MAINNET = 1506
    SHERPAX_TESTNET = 1507
    BEAGLE_MESSAGING_CHAIN = 1515
    TENET = 1559
    CATECOIN_CHAIN_MAINNET = 1618
    ATHEIOS = 1620
    BTACHAIN = 1657
    LIQUICHAIN = 1662
    HORIZEN_GOBI_TESTNET = 1663
    LUDAN_MAINNET = 1688
    ANYTYPE_EVM_CHAIN = 1701
    TBSI_MAINNET = 1707
    TBSI_TESTNET = 1708
    PALETTE_CHAIN_MAINNET = 1718
    REYA_NETWORK = 1729
    PARTYCHAIN = 1773
    GAUSS_MAINNET = 1777
    KERLEANO = 1804
    RABBIT_ANALOG_TESTNET_CHAIN = 1807
    CUBE_CHAIN_MAINNET = 1818
    CUBE_CHAIN_TESTNET = 1819
    RUBY_SMART_CHAIN_MAINNET = 1821
    TESLAFUNDS = 1856
    WHITEBIT_NETWORK = 1875
    GITSHOCK_CARTENZ_TESTNET = 1881
    LIGHTLINK_PHOENIX_MAINNET = 1890
    LIGHTLINK_PEGASUS_TESTNET = 1891
    BON_NETWORK = 1898
    SPORTS_CHAIN_NETWORK = 1904
    BITCICHAIN_MAINNET = 1907
    BITCICHAIN_TESTNET = 1908
    MERKLE_SCAN = 1909
    SCALIND = 1911
    RUBY_SMART_CHAIN_TESTNET = 1912
    ONUS_CHAIN_TESTNET = 1945
    D_CHAIN_MAINNET = 1951
    DEXILLA_TESTNET = 1954
    ELEANOR = 1967
    SUPER_SMART_CHAIN_TESTNET = 1969
    SUPER_SMART_CHAIN_MAINNET = 1970
    ATELIER = 1971
    REDECOIN = 1972
    ONUS_CHAIN_MAINNET = 1975
    EURUS_TESTNET = 1984
    SATOSHIE = 1985
    SATOSHIE_TESTNET = 1986
    ETHERGEM = 1987
    EKTA = 1994
    EDEXA_TESTNET = 1995
    KYOTO_TESTNET = 1998
    DOGECHAIN_MAINNET = 2000
    MILKOMEDA_C1_MAINNET = 2001
    MILKOMEDA_A1_MAINNET = 2002
    CLOUDWALK_TESTNET = 2008
    CLOUDWALK_MAINNET = 2009
    MAINNETZ_MAINNET = 2016
    PUBLICMINT_DEVNET = 2018
    PUBLICMINT_TESTNET = 2019
    PUBLICMINT_MAINNET = 2020
    EDGEWARE_EDGEEVM_MAINNET = 2021
    BERESHEET_BEREEVM_TESTNET = 2022
    TAYCAN_TESTNET = 2023
    RANGERS_PROTOCOL_MAINNET = 2025
    CENTRIFUGE = 2031
    CATALYST = 2032
    PHALA_NETWORK = 2035
    KIWI_SUBNET = 2037
    SHRAPNEL_TESTNET = 2038
    ALEPH_ZERO_TESTNET = 2039
    ORIGINTRAIL_PARACHAIN = 2043
    SHRAPNEL_SUBNET = 2044
    STRATOS_TESTNET = 2047
    STRATOS = 2048
    MOVO_SMART_CHAIN_MAINNET = 2049
    QUOKKACOIN_MAINNET = 2077
    ALTAIR = 2088
    ALGOL = 2089
    ECOBALL_MAINNET = 2100
    ECOBALL_TESTNET_ESPUMA = 2101
    EXOSAMA_NETWORK = 2109
    METAPLAYERONE_MAINNET = 2122
    METAPLAYERONE_DUBAI_TESTNET = 2124
    BIGSHORTBETS = 2137
    DEFI_ORACLE_META_TESTNET = 2138
    BOSAGORA_MAINNET = 2151
    FINDORA_MAINNET = 2152
    FINDORA_TESTNET = 2153
    FINDORA_FORGE = 2154
    SNAXCHAIN_MAINNET = 2192
    MOONSAMA_NETWORK = 2199
    ANTOFY_MAINNET = 2202
    BITCOIN_EVM = 2203
    EVANESCO_MAINNET = 2213
    KAVA_TESTNET = 2221
    KAVA = 2222
    VCHAIN_MAINNET = 2223
    KREST_NETWORK = 2241
    BOMB_CHAIN = 2300
    EBRO_NETWORK = 2306
    AREVIA = 2309
    SOMA_NETWORK_TESTNET = 2323
    ALTCOINCHAIN = 2330
    RSS3_VSL_SEPOLIA_TESTNET = 2331
    SOMA_NETWORK_MAINNET = 2332
    _DEPRECATED_KROMA_SEPOLIA = 2357
    KROMA_SEPOLIA = 2358
    BOMB_CHAIN_TESTNET = 2399
    TCG_VERSE_MAINNET = 2400
    XODEX = 2415
    HYBRID_CHAIN_NETWORK_TESTNET = 2458
    HYBRID_CHAIN_NETWORK_MAINNET = 2468
    UNICORN_ULTRA_NEBULAS_TESTNET = 2484
    FRAXTAL_TESTNET = 2522
    FRAXTAL_SEPOLIA = 2523
    KORTHO_MAINNET = 2559
    TECHPAY_MAINNET = 2569
    POCRNET = 2606
    REDLIGHT_CHAIN_MAINNET = 2611
    EZCHAIN_C_CHAIN_MAINNET = 2612
    EZCHAIN_C_CHAIN_TESTNET = 2613
    WHITEBIT_NETWORK_TESTNET = 2625
    MORPH_TESTNET = 2710
    K_LAOS = 2718
    MORPH_HOLESKY = 2810
    BOBA_NETWORK_GOERLI_TESTNET = 2888
    BITYUAN_MAINNET = 2999
    CENNZNET_RATA = 3000
    CENNZNET_NIKAU = 3001
    CANXIUM_MAINNET = 3003
    PLAYA3ULL_GAMES = 3011
    ORLANDO_CHAIN = 3031
    BIFROST_MAINNET = 3068
    IMMU3_EVM = 3100
    VULTURE_EVM_BETA = 3102
    FILECOIN_HYPERSPACE_TESTNET = 3141
    DUBXCOIN_NETWORK = 3269
    DUBXCOIN_TESTNET = 3270
    DEBOUNCE_SUBNET_TESTNET = 3306
    ZCORE_TESTNET = 3331
    WEB3Q_TESTNET = 3333
    WEB3Q_GALILEO = 3334
    PARIBU_NET_MAINNET = 3400
    SECURECHAIN_TESTNET = 3434
    PARIBU_NET_TESTNET = 3500
    JFIN_CHAIN = 3501
    PANDOPROJECT_MAINNET = 3601
    PANDOPROJECT_TESTNET = 3602
    BOTANIX_TESTNET = 3636
    BOTANIX_MAINNET = 3637
    ICHAIN_NETWORK = 3639
    JOULEVERSE_MAINNET = 3666
    BITTEX_MAINNET = 3690
    EMPIRE_NETWORK = 3693
    SENJEPOWERS_TESTNET = 3698
    SENJEPOWERS_MAINNET = 3699
    XPLA_TESTNET = 3701
    CROSSBELL = 3737
    ASTAR_ZKEVM = 3776
    ALVEYCHAIN_MAINNET = 3797
    TANGLE_TESTNET = 3799
    FIRECHAIN_ZKEVM_GHOSTRIDER = 3885
    KALYCHAIN_MAINNET = 3888
    KALYCHAIN_TESTNET = 3889
    DRAC_NETWORK = 3912
    DOS_TESNET = 3939
    DYNO_MAINNET = 3966
    DYNO_TESTNET = 3967
    YUANCHAIN_MAINNET = 3999
    OZONE_CHAIN_MAINNET = 4000
    PEPERIUM_CHAIN_TESTNET = 4001
    FANTOM_TESTNET = 4002
    X1_FASTNET = 4003
    BOBAOPERA_TESTNET = 4051
    NAHMII_3_MAINNET = 4061
    NAHMII_3_TESTNET = 4062
    MUSTER_MAINNET = 4078
    FASTEX_CHAIN_BAHAMUT_OASIS_TESTNET = 4090
    BITINDI_TESTNET = 4096
    BITINDI_MAINNET = 4099
    AIOZ_NETWORK_TESTNET = 4102
    HUMANS_AI_TESTNET = 4139
    TIPBOXCOIN_TESTNET = 4141
    CROSSFI_TESTNET = 4157
    PHI_NETWORK_V1 = 4181
    LUKSO_TESTNET = 4201
    LISK_SEPOLIA_TESTNET = 4202
    NEXI_MAINNET = 4242
    NEXI_V2_MAINNET = 4243
    BOBAFUJI_TESTNET = 4328
    BEAM = 4337
    CREDIT_SMART_CHAIN_MAINNET = 4400
    HTMLCOIN_MAINNET = 4444
    ORDERLY_SEPOLIA_TESTNET = 4460
    IOTEX_NETWORK_MAINNET = 4689
    IOTEX_NETWORK_TESTNET = 4690
    MEVERSE_CHAIN_TESTNET = 4759
    BLACKFORT_EXCHANGE_NETWORK_TESTNET = 4777
    GLOBEL_CHAIN = 4893
    VENIDIUM_TESTNET = 4918
    VENIDIUM_MAINNET = 4919
    BLACKFORT_EXCHANGE_NETWORK = 4999
    MANTLE = 5000
    MANTLE_TESTNET = 5001
    TREASURENET_MAINNET_ALPHA = 5002
    MANTLE_SEPOLIA_TESTNET = 5003
    TREASURENET_TESTNET = 5005
    BAHAMUT = 5165
    SMART_LAYER_NETWORK = 5169
    TLCHAIN_NETWORK_MAINNET = 5177
    ERASWAP_MAINNET = 5197
    HUMANODE_MAINNET = 5234
    FIRECHAIN_MAINNET_OLD = 5290
    UZMI_NETWORK_MAINNET = 5315
    TRITANIUM_TESTNET = 5353
    VEX_EVM_TESTNET = 5522
    NAHMII_MAINNET = 5551
    NAHMII_TESTNET = 5553
    CHAIN_VERSE_MAINNET = 5555
    OPBNB_TESTNET = 5611
    ARCTURUS_CHAIN_TESTNET = 5616
    TANSSI_EVM_CONTAINERCHAIN = 5678
    SYSCOIN_TANENBAUM_TESTNET = 5700
    HIKA_NETWORK_TESTNET = 5729
    SATOSHICHAIN_TESTNET = 5758
    ONTOLOGY_TESTNET = 5851
    WEGOCHAIN_RUBIDIUM_MAINNET = 5869
    TRES_TESTNET = 6065
    TRES_MAINNET = 6066
    CASCADIA_TESTNET = 6102
    UPTN_TESTNET = 6118
    UPTN = 6119
    DIGIT_SOUL_SMART_CHAIN = 6363
    EVERCLEAR_SEPOLIA = 6398
    EVERCLEAR_MAINNET = 25327
    PEERPAY = 6502
    SCOLCOIN_WEICHAIN_TESTNET = 6552
    FOX_TESTNET_NETWORK = 6565
    PIXIE_CHAIN_MAINNET = 6626
    LATEST_CHAIN_TESTNET = 6660
    CYBRIA_MAINNET = 6661
    CYBRIA_TESTNET = 6666
    IRISHUB = 6688
    PAXB_MAINNET = 6701
    COMPVERSE_MAINNET = 6779
    GOLD_SMART_CHAIN_MAINNET = 6789
    TOMB_CHAIN_MAINNET = 6969
    POLYSMARTCHAIN = 6999
    ZETACHAIN_MAINNET = 7000
    ZETACHAIN_ATHENS_3_TESTNET = 7001
    ELLA_THE_HEART = 7027
    PLANQ_MAINNET = 7070
    NUME = 7100
    HELP_THE_HOMELESS = 7118
    BITROCK_MAINNET = 7171
    KLYNTAR = 7331
    HORIZEN_EON_MAINNET = 7332
    SHYFT_MAINNET = 7341
    RABA_NETWORK_MAINNET = 7484
    MEVERSE_CHAIN_MAINNET = 7518
    CYBER_MAINNET = 7560
    ADIL_TESTNET = 7575
    ADIL_CHAIN_V2_MAINNET = 7576
    THE_ROOT_NETWORK_MAINNET = 7668
    THE_ROOT_NETWORK_PORCINI_TESTNET = 7672
    CANTO = 7700
    CANTO_TESNET = 7701
    BITROCK_TESTNET = 7771
    RISE_OF_THE_WARBOTS_TESTNET = 7777
    MAALCHAIN_TESTNET = 7860
    HAZLOR_TESTNET = 7878
    ARDENIUM_ATHENA = 7895
    DOS_CHAIN = 7979
    TELEPORT = 8000
    TELEPORT_TESTNET = 8001
    MDGL_TESTNET = 8029
    SHARDEUM_LIBERTY_1_X = 8080
    SHARDEUM_LIBERTY_2_X = 8081
    SHARDEUM_SPHINX_1_X = 8082
    BITCOIN_CHAIN = 8086
    E_DOLLAR = 8087
    STREAMUX_BLOCKCHAIN = 8098
    QITMEER_NETWORK_TESTNET = 8131
    QITMEER_NETWORK_MIXNET = 8132
    QITMEER_NETWORK_PRIVNET = 8133
    AMANA = 8134
    FLANA = 8135
    MIZANA = 8136
    TESTNET_BEONE_CHAIN = 8181
    TORUS_MAINNET = 8192
    TORUS_TESTNET = 8194
    KLAYTN_MAINNET_CYPRESS = 8217
    BLOCKTON_BLOCKCHAIN = 8272
    KORTHOTEST = 8285
    LORENZO = 8329
    DRACONES_FINANCIAL_SERVICES = 8387
    BASE = 8453
    TOKI_NETWORK = 8654
    TOKI_TESTNET = 8655
    HELA_OFFICIAL_RUNTIME_MAINNET = 8668
    TOOL_GLOBAL_MAINNET = 8723
    TOOL_GLOBAL_TESTNET = 8724
    STORAGECHAIN_MAINNET = 8726
    STORAGECHAIN_TESTNET = 8727
    ALPH_NETWORK = 8738
    TMY_CHAIN = 8768
    IOTA_EVM = 8822
    MARO_BLOCKCHAIN_MAINNET = 8848
    UNIQUE = 8880
    QUARTZ_BY_UNIQUE = 8881
    OPAL_TESTNET_BY_UNIQUE = 8882
    SAPPHIRE_BY_UNIQUE = 8883
    XANACHAIN = 8888
    VYVO_SMART_CHAIN = 8889
    MAMMOTH_MAINNET = 8898
    JIBCHAIN_L1 = 8899
    GIANT_MAMMOTH_MAINNET = 8989
    BLOXBERG = 8995
    EVMOS_TESTNET = 9000
    EVMOS = 9001
    BERYLBIT_MAINNET = 9012
    GENESIS_COIN = 9100
    RINIA_TESTNET_OLD = 9170
    CODEFIN_MAINNET = 9223
    DOGCOIN_TESTNET = 9339
    EVOKE_MAINNET = 9395
    RANGERS_PROTOCOL_TESTNET_ROBIN = 9527
    QEASYWEB3_TESTNET = 9528
    NEONLINK_TESTNET = 9559
    OORT_MAINNETDEV = 9700
    BOBA_BNB_TESTNET = 9728
    MAINNETZ_TESTNET = 9768
    PEPENETWORK_MAINNET = 9779
    CARBON_EVM = 9790
    CARBON_EVM_TESTNET = 9792
    IMPERIUM_TESTNET = 9818
    IMPERIUM_MAINNET = 9819
    DOGELAYER_MAINNET = 9888
    MIND_SMART_CHAIN_TESTNET = 9977
    COMBO_MAINNET = 9980
    AGUNG_NETWORK = 9990
    MIND_SMART_CHAIN_MAINNET = 9996
    ALTLAYER_TESTNET = 9997
    MYOWN_TESTNET = 9999
    SMART_BITCOIN_CASH = 10000
    SMART_BITCOIN_CASH_TESTNET = 10001
    GON_CHAIN = 10024
    JAPAN_OPEN_CHAIN_TESTNET = 10081
    SJATSH = 10086
    BLOCKCHAIN_GENESIS_MAINNET = 10101
    GNOSIS_CHIADO_TESTNET = 10200
    MAXXCHAIN_MAINNET = 10201
    ARTHERA_MAINNET = 10242
    ARTHERA_TESTNET = 10243
    _0XTADE = 10248
    WORLDLAND_TESTNET = 10395
    NUMBERS_MAINNET = 10507
    NUMBERS_TESTNET = 10508
    CRYPTOCOINPAY = 10823
    QUADRANS_BLOCKCHAIN = 10946
    QUADRANS_BLOCKCHAIN_TESTNET = 10947
    ASTRA = 11110
    WAGMI = 11111
    ASTRA_TESTNET = 11115
    HASHBIT_MAINNET = 11119
    HAQQ_NETWORK = 11235
    SHYFT_TESTNET = 11437
    SARDIS_TESTNET = 11612
    SANR_CHAIN = 11888
    POLYGON_SUPERNET_ARIANEE = 11891
    SATOSHICHAIN_MAINNET = 12009
    SINGULARITY_ZERO_TESTNET = 12051
    SINGULARITY_ZERO_MAINNET = 12052
    BRC_CHAIN_MAINNET = 12123
    FIBONACCI_MAINNET = 12306
    BLG_TESTNET = 12321
    STEP_TESTNET = 12345
    RSS3_VSL_MAINNET = 12553
    RIKEZA_NETWORK_TESTNET = 12715
    QUANTUM_CHAIN_TESTNET = 12890
    SPS = 13000
    CREDIT_SMART_CHAIN = 13308
    BEAM_TESTNET = 13337
    IMMUTABLE_ZKEVM = 13371
    PHOENIX_MAINNET = 13381
    IMMUTABLE_ZKEVM_TESTNET = 13473
    SUSONO = 13812
    SPS_TESTNET = 14000
    HUMANODE_TESTNET_5_ISRAFEL = 14853
    IMMUTABLE_ZKEVM_DEVNET = 15003
    LOOPNETWORK_MAINNET = 15551
    TRUST_EVM_TESTNET = 15555
    EOS_EVM_NETWORK_TESTNET = 15557
    METADOT_MAINNET = 16000
    METADOT_TESTNET = 16001
    GENESYS_MAINNET = 16507
    IRISHUB_TESTNET = 16688
    AIRDAO_MAINNET = 16718
    IVAR_CHAIN_TESTNET = 16888
    HOLESKY = 17000
    REDSTONE_HOLESKY_TESTNET = 17001
    GARNET_HOLESKY = 17069
    G8CHAIN_MAINNET = 17171
    PALETTE_CHAIN_TESTNET = 17180
    EOS_EVM_NETWORK = 17777
    FRONTIER_OF_DREAMS_TESTNET = 18000
    SMART_TRADE_NETWORKS = 18122
    PROOF_OF_MEMES = 18159
    G8CHAIN_TESTNET = 18181
    UNREAL_TESTNET = 18231
    UNREAL = 18233
    MXC_ZKEVM_MAINNET = 18686
    HOME_VERSE_MAINNET = 19011
    BTCIX_NETWORK = 19845
    CAMELARK_MAINNET = 20001
    CALLISTO_TESTNET = 20729
    P12_CHAIN = 20736
    CENNZNET_AZALEA = 21337
    OMCHAIN_MAINNET = 21816
    BSL_MAINNET = 21912
    TAYCAN = 22023
    AIRDAO_TESTNET = 22040
    NAUTILUS_MAINNET = 22222
    GOLDXCHAIN_TESTNET = 22324
    MAP_MAINNET = 22776
    ANTOFY_TESTNET = 23006
    OPSIDE_TESTNET = 23118
    OASIS_SAPPHIRE = 23294
    OASIS_SAPPHIRE_TESTNET = 23295
    BLAST_TESTNET = 23888
    WEBCHAIN = 24484
    MINTME_COM_COIN = 24734
    HAMMER_CHAIN_MAINNET = 25888
    BITKUB_CHAIN_TESTNET = 25925
    FERRUM_TESTNET = 26026
    HERTZ_NETWORK_MAINNET = 26600
    OASISCHAIN_MAINNET = 26863
    OPTIMISM_BEDROCK_GOERLI_ALPHA_TESTNET = 28528
    MCH_VERSE_MAINNET = 29548
    PIECE_TESTNET = 30067
    CERIUM_TESTNET = 30103
    ETHERSOCIAL_NETWORK = 31102
    CLOUDTX_MAINNET = 31223
    CLOUDTX_TESTNET = 31224
    GOCHAIN_TESTNET = 31337
    EVOKE_TESTNET = 31414
    FILECOIN_WALLABY_TESTNET = 31415
    W3GAMEZ_HOLESKY_TESTNET = 32001
    BITGERT_MAINNET = 32520
    FUSION_MAINNET = 32659
    ZILLIQA_EVM = 32769
    ZILLIQA_EVM_ISOLATED_SERVER = 32990
    ZILLIQA_EVM_TESTNET = 33101
    CLOUDVERSE_SUBNET = 33210
    AVES_MAINNET = 33333
    ZILLIQA_EVM_DEVNET = 33385
    ZILLIQA_2_EVM_DEVNET = 33469
    MODE = 34443
    J2O_TARO = 35011
    Q_MAINNET = 35441
    Q_TESTNET = 35443
    CONNECTORMANAGER = 38400
    CONNECTORMANAGER_ROBIN = 38401
    ENERGI_MAINNET = 39797
    OHO_MAINNET = 39815
    ALEPH_ZERO = 41455
    OPULENT_X_BETA = 41500
    PEGGLECOIN = 42069
    ARBITRUM_ONE = 42161
    ARBITRUM_NOVA = 42170
    CELO_MAINNET = 42220
    OASIS_EMERALD_TESTNET = 42261
    OASIS_EMERALD = 42262
    GOLDXCHAIN_MAINNET = 42355
    ZKFAIR_MAINNET = 42766
    ETHERLINK_MAINNET = 42793
    GESOTEN_VERSE_TESTNET = 42801
    KINTO_TESTNET = 42888
    ATHEREUM = 43110
    AVALANCHE_FUJI_TESTNET = 43113
    AVALANCHE_C_CHAIN = 43114
    BOBA_AVAX = 43288
    ZKFAIR_TESTNET = 43851
    FRENCHAIN = 44444
    CELO_ALFAJORES_TESTNET = 44787
    AUTOBAHN_NETWORK = 45000
    DEELANCE_MAINNET = 45510
    FUSION_TESTNET = 46688
    REI_NETWORK = 47805
    ZIRCUIT_TESTNET = 48899
    WIRESHAPE_FLORIPA_TESTNET = 49049
    BIFROST_TESTNET = 49088
    ENERGI_TESTNET = 49797
    LIVEPLEX_ORACLEEVM = 50001
    YOOLDO_VERSE_MAINNET = 50005
    YOOLDO_VERSE_TESTNET = 50006
    GTON_TESTNET = 50021
    LUMOZ_TESTNET_ALPHA = 51178
    SARDIS_MAINNET = 51712
    ELECTRONEUM_MAINNET = 52014
    DODOCHAIN_TESTNET = 53457
    DFK_CHAIN = 53935
    HAQQ_CHAIN_TESTNET = 54211
    TORONET_TESTNET = 54321
    TITAN = 55004
    REI_CHAIN_MAINNET = 55555
    REI_CHAIN_TESTNET = 55556
    BOBA_BNB_MAINNET = 56288
    VELO_LABS_MAINNET = 56789
    ROLLUX_TESTNET = 57000
    SEPOLIA_PGN_PUBLIC_GOODS_NETWORK = 58008
    LINEA_SEPOLIA = 59141
    LINEA = 59144
    GENESYS_CODE_MAINNET = 59971
    THINKIUM_TESTNET_CHAIN_0 = 60000
    THINKIUM_TESTNET_CHAIN_1 = 60001
    THINKIUM_TESTNET_CHAIN_2 = 60002
    THINKIUM_TESTNET_CHAIN_103 = 60103
    BOB = 60808
    AXELCHAIN_DEV_NET = 61800
    ETICA_MAINNET = 61803
    DOKEN_SUPER_CHAIN_MAINNET = 61916
    CELO_BAKLAVA_TESTNET = 62320
    MULTIVAC_MAINNET = 62621
    ECREDITS_MAINNET = 63000
    ECREDITS_TESTNET = 63001
    SCOLCOIN_MAINNET = 65450
    JANUS_TESTNET = 66988
    SIRIUSNET = 67390
    COSMIC_CHAIN = 67588
    DM2_VERSE_MAINNET = 68770
    CONDRIEU = 69420
    THINKIUM_MAINNET_CHAIN_0 = 70000
    THINKIUM_MAINNET_CHAIN_1 = 70001
    THINKIUM_MAINNET_CHAIN_2 = 70002
    THINKIUM_MAINNET_CHAIN_103 = 70103
    GUAPCOINX = 71111
    POLYJUICE_TESTNET = 71393
    GODWOKEN_TESTNET_V1 = 71401
    GODWOKEN_MAINNET = 71402
    GROK_CHAIN_MAINNET = 72992
    ENERGY_WEB_VOLTA_TESTNET = 73799
    MIXIN_VIRTUAL_MACHINE = 73927
    RESINCOIN_MAINNET = 75000
    FOUNDRY_CHAIN_TESTNET = 77238
    VENTION_SMART_CHAIN_MAINNET = 77612
    TORONET_MAINNET = 77777
    FIRENZE_TEST_NETWORK = 78110
    DRAGONFLY_MAINNET_HEXAPOD = 78281
    AMPLIFY_SUBNET = 78430
    BULLETIN_SUBNET = 78431
    CONDUIT_SUBNET = 78432
    GOLD_SMART_CHAIN_TESTNET = 79879
    MUMBAI = 80001
    AMOY = 80002
    BERACHAIN_BARTIO = 80084
    BERACHAIN_ARTIO = 80085
    NORDEK_MAINNET = 81041
    AMANA_TESTNET = 81341
    AMANA_MIXNET = 81342
    AMANA_PRIVNET = 81343
    FLANA_TESTNET = 81351
    FLANA_MIXNET = 81352
    FLANA_PRIVNET = 81353
    MIZANA_TESTNET = 81361
    MIZANA_MIXNET = 81362
    MIZANA_PRIVNET = 81363
    BLAST = 81457
    QUANTUM_CHAIN_MAINNET = 81720
    SMART_LAYER_NETWORK_TESTNET = 82459
    BASE_GOERLI_TESTNET = 84531
    BASE_SEPOLIA_TESTNET = 84532
    AERIE_NETWORK = 84886
    CYBERTRUST = 85449
    NAUTILUS_PROTEUS_TESTNET = 88002
    CHILIZ_SCOVILLE_TESTNET = 88880
    IVAR_CHAIN_MAINNET = 88888
    F_XCORE_TESTNET_NETWORK = 90001
    BEVERLY_HILLS = 90210
    NAUTILUS_TRITION_CHAIN = 91002
    COMBO_TESTNET = 91715
    LAMBDA_TESTNET = 92001
    MANTIS_TESTNET_HEXAPOD = 96970
    BOBA_BNB_MAINNET_OLD = 97288
    ELIBERTY_TESTNET = 99099
    UB_SMART_CHAIN_TESTNET = 99998
    UB_SMART_CHAIN = 99999
    QUARKCHAIN_MAINNET_ROOT = 100000
    QUARKCHAIN_MAINNET_SHARD_0 = 100001
    QUARKCHAIN_MAINNET_SHARD_1 = 100002
    QUARKCHAIN_MAINNET_SHARD_2 = 100003
    QUARKCHAIN_MAINNET_SHARD_3 = 100004
    QUARKCHAIN_MAINNET_SHARD_4 = 100005
    QUARKCHAIN_MAINNET_SHARD_5 = 100006
    QUARKCHAIN_MAINNET_SHARD_6 = 100007
    QUARKCHAIN_MAINNET_SHARD_7 = 100008
    VECHAIN = 100009
    VECHAIN_TESTNET = 100010
    DEPRECATED_CHI = 100100
    SOVERUN_TESTNET = 101010
    CRYSTALEUM = 103090
    STRATIS_MAINNET = 105105
    BROCHAIN_MAINNET = 108801
    QUARKCHAIN_DEVNET_ROOT = 110000
    QUARKCHAIN_DEVNET_SHARD_0 = 110001
    QUARKCHAIN_DEVNET_SHARD_1 = 110002
    QUARKCHAIN_DEVNET_SHARD_2 = 110003
    QUARKCHAIN_DEVNET_SHARD_3 = 110004
    QUARKCHAIN_DEVNET_SHARD_4 = 110005
    QUARKCHAIN_DEVNET_SHARD_5 = 110006
    QUARKCHAIN_DEVNET_SHARD_6 = 110007
    QUARKCHAIN_DEVNET_SHARD_7 = 110008
    SIBERIUM_TEST_NETWORK = 111000
    SIBERIUM_NETWORK = 111111
    REAL_MAINNET = 111188
    METACHAIN_ONE_MAINNET = 112358
    ADIL_DEVNET = 123456
    ETHERLINK_TESTNET = 128123
    ETND_CHAIN_MAINNETS = 131419
    ICPLAZA_MAINNET = 142857
    TAIKO_MAINNET = 167000
    TAIKO_ALPHA_2_TESTNET = 167004
    TAIKO_GRIMSVOTN_L2 = 167005
    TAIKO_ELDFELL_L3 = 167006
    TAIKO_JOLNIR_L2 = 167007
    TAIKO_HEKLA_L2 = 167009
    BITICA_CHAIN_MAINNET = 188710
    CONDOR_TEST_NETWORK = 188881
    MILKOMEDA_C1_TESTNET = 200101
    MILKOMEDA_A1_TESTNET = 200202
    AKROMA = 200625
    ALAYA_MAINNET = 201018
    ALAYA_DEV_TESTNET = 201030
    MYTHICAL_CHAIN = 201804
    DECIMAL_SMART_CHAIN_TESTNET = 202020
    X1_DEVNET = 202212
    JELLIE = 202624
    X1_NETWORK = 204005
    AURORIA_TESTNET = 205205
    PLATON_MAINNET = 210425
    MAS_MAINNET = 220315
    REAPCHAIN_MAINNET = 221230
    REAPCHAIN_TESTNET = 221231
    TAF_ECO_CHAIN_MAINNET = 224168
    CONET_SEBOLIA_TESTNET = 224422
    CONET_HOLESKY = 224433
    HASHKEY_CHAIN_TESTNET = 230315
    HAYMO_TESTNET = 234666
    ARTIS_SIGMA1 = 246529
    ARTIS_TESTNET_TAU1 = 246785
    SAAKURU_TESTNET = 247253
    CMP_MAINNET = 256256
    GEAR_ZERO_NETWORK_TESTNET = 266256
    EGONCOIN_TESTNET = 271271
    SOCIAL_SMART_CHAIN_MAINNET = 281121
    FILECOIN_CALIBRATION_TESTNET = 314159
    TTCOIN_SMART_CHAIN_MAINNET = 330844
    AVES_TESTNET = 333331
    NATIV3_TESTNET = 333333
    OONE_CHAIN_TESTNET = 333666
    OONE_CHAIN_DEVNET = 333777
    POLIS_TESTNET = 333888
    POLIS_MAINNET = 333999
    BITFINITY_NETWORK_TESTNET = 355113
    DIGIT_SOUL_SMART_CHAIN_2 = 363636
    HAPCHAIN_TESTNET = 373737
    METAL_C_CHAIN = 381931
    METAL_TAHOE_C_CHAIN = 381932
    TIPBOXCOIN_MAINNET = 404040
    KEKCHAIN = 420420
    KEKCHAIN_KEKTEST = 420666
    ALTERIUM_L2_TESTNET = 420692
    ARBITRUM_RINKEBY = 421611
    ARBITRUM_GOERLI = 421613
    ARBITRUM_SEPOLIA = 421614
    FASTEX_CHAIN_TESTNET = 424242
    MARKR_GO = 431140
    DEXALOT_SUBNET_TESTNET = 432201
    DEXALOT_SUBNET = 432204
    WEELINK_TESTNET = 444900
    PATEX_SEPOLIA_TESTNET = 471100
    ULTRA_PRO_MAINNET = 473861
    OPENCHAIN_MAINNET = 474142
    AUTONOMOUS_TESTNET = 490000
    CMP_TESTNET = 512512
    ETHEREUM_FAIR = 513100
    SCROLL_SEPOLIA_TESTNET = 534351
    SCROLL = 534352
    SCROLL_ALPHA_TESTNET = 534353
    SCROLL_PRE_ALPHA_TESTNET = 534354
    SHINARIUM_BETA = 534849
    BEANECO_SMARTCHAIN = 535037
    HYPRA_MAINNET = 622277
    BEAR_NETWORK_CHAIN_MAINNET = 641230
    ALL_MAINNET = 651940
    OPEN_CAMPUS_CODEX = 656476
    XAI = 660279
    VISION_VPIONEER_TEST_CHAIN = 666666
    HELA_OFFICIAL_RUNTIME_TESTNET = 666888
    SEI_DEVNET = 713715
    BEAR_NETWORK_CHAIN_TESTNET = 751230
    MIEXS_SMARTCHAIN = 761412
    MODULARIUM = 776877
    OCTASPACE = 800001
    ZKLINK_NOVA = 810180
    ZKLINK_NOVA_GOERLI = 810182
    CURVE_MAINNET = 827431
    _4GOODNETWORK = 846000
    DODAO = 855456
    BLOCX_MAINNET = 879151
    VISION_MAINNET = 888888
    POSICHAIN_MAINNET_SHARD_0 = 900000
    POSICHAIN_TESTNET_SHARD_0 = 910000
    ASTRIA_EVM_DUSKNET = 912559
    POSICHAIN_DEVNET_SHARD_0 = 920000
    POSICHAIN_DEVNET_SHARD_1 = 920001
    FNCY_TESTNET = 923018
    ELUVIO_CONTENT_FABRIC = 955305
    ECROX_CHAIN_MAINNET = 988207
    TILTYARD_SUBNET = 1127469
    ZKATANA = 1261120
    ETHO_PROTOCOL = 1313114
    XEROM = 1313500
    KINTSUGI = 1337702
    KILN = 1337802
    ZHEJIANG = 1337803
    TURKEY_DEMO_DEV = 1731313
    DEBANK_TESTNET = 2021398
    PLIAN_MAINNET_MAIN = 2099156
    PLATON_DEV_TESTNET_DEPRECATED = 2203181
    PLATON_DEV_TESTNET2 = 2206132
    DPU_CHAIN = 2611555
    FILECOIN_BUTTERFLY_TESTNET = 3141592
    MANTA_PACIFIC_TESTNET = 3441005
    ALTLAYER_ZERO_GAS_NETWORK = 4000003
    WORLDS_CALDERA = 4281033
    MXC_WANNSEE_ZKEVM_TESTNET = 5167003
    ELECTRONEUM_TESTNET = 5201420
    IMVERSED_MAINNET = 5555555
    IMVERSED_TESTNET = 5555558
    ASTAR_ZKYOTO = 6038361
    SAAKURU_MAINNET = 7225878
    OPENVESSEL = 7355310
    QL1_TESTNET = 7668378
    MUSICOIN = 7762959
    ZORA = 7777777
    PLIAN_MAINNET_SUBCHAIN_1 = 8007736
    HOKUM = 8080808
    HAPCHAIN = 8794598
    QUARIX_TESTNET = 8888881
    QUARIX = 8888888
    XCAP = 9322252
    MILVINE = 9322253
    PLIAN_TESTNET_SUBCHAIN_1 = 10067275
    SOVERUN_MAINNET = 10101010
    SEPOLIA = 11155111
    OP_SEPOLIA_TESTNET = 11155420
    PEPCHAIN_CHURCHILL = 13371337
    ANDUSCHAIN_MAINNET = 14288640
    PLIAN_TESTNET_MAIN = 16658437
    IOLITE = 18289463
    SMARTMESH_MAINNET = 20180430
    QUARKBLOCKCHAIN = 20181205
    PEGO_NETWORK = 20201022
    HOKUM_TESTNET = 20482050
    EXCELON_MAINNET = 22052002
    EXCOINCIAL_CHAIN_VOLTA_TESTNET = 27082017
    EXCOINCIAL_CHAIN_MAINNET = 27082022
    ANCIENT8_TESTNET = 28122024
    AUXILIUM_NETWORK_MAINNET = 28945486
    FLACHAIN_MAINNET = 29032022
    FILECOIN_LOCAL_TESTNET = 31415926
    JOYS_DIGITAL_MAINNET = 35855456
    MAISTESTSUBNET = 43214913
    AQUACHAIN = 61717561
    AUTONITY_BAKERLOO_THAMES_TESTNET = 65010000
    AUTONITY_BAKERLOO_BARADA_TESTNET = 65010001
    AUTONITY_PICCADILLY_THAMES_TESTNET = 65100000
    AUTONITY_PICCADILLY_BARADA_TESTNET = 65100001
    FRAME_TESTNET = 68840142
    T_E_A_M_BLOCKCHAIN = 88888888
    POLYGON_BLACKBERRY = 94204209
    JOYS_DIGITAL_TESTNET = 99415706
    CYBER_TESTNET = 111557560
    OP_CELESTIA_RASPBERRY = 123420111
    BLAST_SEPOLIA_TESTNET = 168587773
    GATHER_MAINNET_NETWORK = 192837465
    KANAZAWA = 222000222
    NEON_EVM_DEVNET = 245022926
    NEON_EVM_MAINNET = 245022934
    NEON_EVM_TESTNET = 245022940
    RAZOR_SKALE_CHAIN = 278611351
    ONELEDGER_MAINNET = 311752642
    MELD = 333000333
    SKALE_CALYPSO_HUB_TESTNET = 344106930
    GATHER_TESTNET_NETWORK = 356256156
    SKALE_EUROPA_HUB_TESTNET = 476158412
    GATHER_DEVNET_NETWORK = 486217935
    SKALE_NEBULA_HUB_TESTNET = 503129905
    ZORA_SEPOLIA_TESTNET = 999999999
    IPOS_NETWORK = 1122334455
    CYBERDECKNET = 1146703430
    HUMAN_PROTOCOL = 1273227453
    AURORA_MAINNET = 1313161554
    AURORA_TESTNET = 1313161555
    AURORA_BETANET = 1313161556
    SKALE_TITAN_HUB = 1350216234
    CHAOS_SKALE_TESTNET = 1351057110
    RAPTORCHAIN = 1380996178
    SKALE_NEBULA_HUB = 1482601649
    SKALE_TITAN_HUB_TESTNET = 1517929550
    SKALE_CALYPSO_HUB = 1564830818
    HARMONY_MAINNET_SHARD_0 = 1666600000
    HARMONY_MAINNET_SHARD_1 = 1666600001
    HARMONY_MAINNET_SHARD_2 = 1666600002
    HARMONY_MAINNET_SHARD_3 = 1666600003
    HARMONY_TESTNET_SHARD_0 = 1666700000
    HARMONY_TESTNET_SHARD_1 = 1666700001
    HARMONY_DEVNET_SHARD_0 = 1666900000
    HARMONY_DEVNET_SHARD_1 = 1666900001
    DATAHOPPER = 2021121117
    SKALE_EUROPA_HUB = 2046399126
    ANCIENT8_TESTNET_DEPRECATED = 2863311531
    PIRL = 3125659152
    ONELEDGER_TESTNET_FRANKENSTEIN = 4216137055
    PALM_TESTNET = 11297108099
    PALM = 11297108109
    XAI_TESTNET = 37714555429
    ARBITRUM_BLUEBERRY = 88153591557
    ALPHABET_MAINNET = 111222333444
    NTITY_MAINNET = 197710212030
    HARADEV_TESTNET = 197710212031
    ZENIQ = 383414847825
    PDC_MAINNET = 666301171999
    MOLEREUM_NETWORK = 6022140761023

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN
