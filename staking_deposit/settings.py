from typing import Dict, NamedTuple
from .version import __version__

DEPOSIT_CLI_VERSION = __version__


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


LUKSO = 'lukso'
LUKSO_TESTNET = 'lukso-testnet'
LUKSO_DEVNET = 'lukso-devnet'
MAINNET = 'ethereum'
ROPSTEN = 'ropsten'
GOERLI = 'goerli'
PRATER = 'prater'
SEPOLIA = 'sepolia'
ZHEJIANG = 'zhejiang'

# LUKSO mainnet setting
LUKSOSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO, GENESIS_FORK_VERSION=bytes.fromhex('42000001'))
# LUKSO testnet setting
LUKSOTestnetSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO_TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('42010001'))
# LUKSO devnet setting
LUKSODevnetSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO_DEVNET, GENESIS_FORK_VERSION=bytes.fromhex('74200001'))
# Ethereum Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'))
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang setting
ZhejiangSetting = BaseChainSetting(
    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    LUKSO: LUKSOSetting,
    LUKSO_TESTNET: LUKSOTestnetSetting,
    LUKSO_DEVNET: LUKSODevnetSetting,
    MAINNET: MainnetSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    SEPOLIA: SepoliaSetting,
    ZHEJIANG: ZhejiangSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
