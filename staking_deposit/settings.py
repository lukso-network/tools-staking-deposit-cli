from typing import Dict, NamedTuple
from .version import __version__

DEPOSIT_CLI_VERSION = __version__


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


LUKSO = 'lukso'
LUKSO_TESTNET = 'lukso-testnet'
MAINNET = 'ethereum'
ROPSTEN = 'ropsten'
GOERLI = 'goerli'
PRATER = 'prater'
KILN = 'kiln'
SEPOLIA = 'sepolia'


# LUKSO mainnet setting
LUKSOSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO, GENESIS_FORK_VERSION=bytes.fromhex('42000001'))
# LUKSO testnet setting
LUKSOTestnetSetting = BaseChainSetting(
    NETWORK_NAME=LUKSO_TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('42010001'))
# Ethereum Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Ropsten setting
RopstenSetting = BaseChainSetting(
    NETWORK_NAME=ROPSTEN, GENESIS_FORK_VERSION=bytes.fromhex('80000069'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
# Merge Testnet (spec v1.1.9)
KilnSetting = BaseChainSetting(
    NETWORK_NAME=KILN, GENESIS_FORK_VERSION=bytes.fromhex('70000069'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'))

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    LUKSO: LUKSOSetting,
    LUKSO_TESTNET: LUKSOTestnetSetting,
    MAINNET: MainnetSetting,
    ROPSTEN: RopstenSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    KILN: KilnSetting,
    SEPOLIA: SepoliaSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
