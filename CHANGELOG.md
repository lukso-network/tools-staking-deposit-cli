# Changelog

## [2.5.7](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.5.6...v2.5.7) (2024-03-14)


### Bug Fixes

* Add manual tests and lints into github actions ([#40](https://github.com/lukso-network/tools-key-gen-cli/issues/40)) ([a6178d5](https://github.com/lukso-network/tools-key-gen-cli/commit/a6178d5f43809816763c8e00a59fa82a3b8821f6))
* Improve argument processing and revert click version ([#38](https://github.com/lukso-network/tools-key-gen-cli/issues/38)) ([1197b4b](https://github.com/lukso-network/tools-key-gen-cli/commit/1197b4b4005fd4694ce613b37b399d6124b77887))

## [2.5.6](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.5.5...v2.5.6) (2023-08-21)


### Bug Fixes

* Cleanup and re-try ([5b5fde5](https://github.com/lukso-network/tools-key-gen-cli/commit/5b5fde5a76d1a2303a531a68aec66344d9762265))
* Universal2 build macos is completely broken for unknown reason ([ebb9622](https://github.com/lukso-network/tools-key-gen-cli/commit/ebb962229a5a56ebe6271483877c0e56ace71c44))

## [2.5.5](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.5.4...v2.5.5) (2023-08-09)


### Bug Fixes

* --amount is no longer a thing ([807c155](https://github.com/lukso-network/tools-key-gen-cli/commit/807c1556cc241603a99810cb913d8ef33f4bf4a4))
* Add a small buildtest.sh script which allows testing of gitops build (mostly useful for MacOS Mx) ([f25b9e6](https://github.com/lukso-network/tools-key-gen-cli/commit/f25b9e686a6a3ba10f867e39170fbf86057ceba6))
* Adjust readme comment for --chain on new bls-to-execution-change sub-command. ([b0c0f91](https://github.com/lukso-network/tools-key-gen-cli/commit/b0c0f91151d9b2bd56c96dc20734b6f2ec37f1e2))
* Docker build. ([92ffb49](https://github.com/lukso-network/tools-key-gen-cli/commit/92ffb491a19f2fed4cb7492f82aab8cddb3ebba6))
* Dockerbuild is not even reproducible locally ([5a5ce84](https://github.com/lukso-network/tools-key-gen-cli/commit/5a5ce846e8cd748bdc3dd6a9a5bf87175c087a7e))
* Fix arg errors in pip ([0c05938](https://github.com/lukso-network/tools-key-gen-cli/commit/0c05938c39389539f09e681870efa0772bf7f0f9))
* Fix pyinstaller by reverting it again ([431475c](https://github.com/lukso-network/tools-key-gen-cli/commit/431475c33e7c0aba99390eed52fa395344bdeacf))
* Install cython, cytoolz and pycryptodome separately in Dockerfile ([1c61905](https://github.com/lukso-network/tools-key-gen-cli/commit/1c619054d35c95191ebffc1d21d62bfc4206548d))
* Move cython and pyinstaller fully global ([55f304a](https://github.com/lukso-network/tools-key-gen-cli/commit/55f304a9299410ae49f416c4ae4a9ac195de6627))
* Now pycryptodome is no longer building on mac ([2bfdcc9](https://github.com/lukso-network/tools-key-gen-cli/commit/2bfdcc9fdc4685f981ca60a24a7cb0da5d677fb8))
* Patch cython build ([9072a07](https://github.com/lukso-network/tools-key-gen-cli/commit/9072a07e5d278037026f14d8f6e65a5a6c13ec1e))
* Patch to specific cython version ([470eeba](https://github.com/lukso-network/tools-key-gen-cli/commit/470eebac8cf75aad604ddd0bc28101151d75c7bb))
* Remove another unused network KILN ([377cf03](https://github.com/lukso-network/tools-key-gen-cli/commit/377cf038d4b0919bf6bbaef02f584b616a8df7da))
* Remove incomplete and unused network settings ([e382bc8](https://github.com/lukso-network/tools-key-gen-cli/commit/e382bc8382214b57d0a9e4949196b3dfbee435ec))
* Remove unused commented out code ([d8bc056](https://github.com/lukso-network/tools-key-gen-cli/commit/d8bc056fa1f119b7331690b157b246384aa25d26))
* Repair requirements_test.txt ([18d6df3](https://github.com/lukso-network/tools-key-gen-cli/commit/18d6df3b4fbb8a08b8367a19631bc791e66d9882))
* Test a way to force using the right cython and cytoolz ([592856c](https://github.com/lukso-network/tools-key-gen-cli/commit/592856c586d17b7741f089a7bde41505fd5f6680))
* try again ([e856b49](https://github.com/lukso-network/tools-key-gen-cli/commit/e856b495798eae70a96b495f24a253b89a24168a))
* Try patch of cytoolz ([5b124b5](https://github.com/lukso-network/tools-key-gen-cli/commit/5b124b52a43d824ba88a963eed528835b6115076))
* Try patch of cytoolz ([b4eba45](https://github.com/lukso-network/tools-key-gen-cli/commit/b4eba451e51188b27da04b0cea96587df6a70990))
* Upgrade python docker to 3.11.4-alpine3.18 ([32857be](https://github.com/lukso-network/tools-key-gen-cli/commit/32857be2009b4aba823cd48f4454000da0bf46da))
* Use non-rooted python installer ([96f83eb](https://github.com/lukso-network/tools-key-gen-cli/commit/96f83eb90d4e8603816e538349f4450c84a5b861))
* Use python 3.11.4 for all archs ([4889ef2](https://github.com/lukso-network/tools-key-gen-cli/commit/4889ef21d4170d72d61d8449a93d9693c5373dc5))

## [2.5.4](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.5.3...v2.5.4) (2023-07-02)


### Bug Fixes

* JITOptions get_default doesn't support new click API, empty args don't diplay help ([cc669cc](https://github.com/lukso-network/tools-key-gen-cli/commit/cc669cc5d0a9c896cf3fb95f075e935ad24cecea))

## [2.5.3](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.5.2...v2.5.3) (2023-05-08)


### Bug Fixes

* -nocytoolz is no more ([2aa05b8](https://github.com/lukso-network/tools-key-gen-cli/commit/2aa05b80e5b01ef243ddfaf804c84f65c48eba4d))
* Also use -nocytoolz here ([8cd0c85](https://github.com/lukso-network/tools-key-gen-cli/commit/8cd0c85a41b18343645678dbc8c0cb5583c8487a))
* Apply python fixes to allow GUI to build ([0c92854](https://github.com/lukso-network/tools-key-gen-cli/commit/0c928541e111b8e70d7fec8bbc3f3ae3f8592d3f))
* local build now that GUI works ([237c6bb](https://github.com/lukso-network/tools-key-gen-cli/commit/237c6bb7fafcc55b2ea760642d5c23369519dca8))
* Make sure all pyinstaller is 5.9 ([8bfb54c](https://github.com/lukso-network/tools-key-gen-cli/commit/8bfb54c04f9b9447ec80f1169d49a41f6e636111))
* More dependencies affected (domino effect) ([8e1fa9a](https://github.com/lukso-network/tools-key-gen-cli/commit/8e1fa9a2307b0736d0b432ebfe8a5b3070c89489))
* Need zlib-dev ([880830f](https://github.com/lukso-network/tools-key-gen-cli/commit/880830f7f41e02bb1747f60942b9080bd57e8087))
* pyinstaller needs zlib in docker. ([bc8701a](https://github.com/lukso-network/tools-key-gen-cli/commit/bc8701a3fec18acd67b353785b621b34b4827a61))
* pyinstaller-hooks-contrib ([4912dad](https://github.com/lukso-network/tools-key-gen-cli/commit/4912dad2e3cfc9eabd6a638a74b430180bd29af2))
* Repair altgraph ([17e325f](https://github.com/lukso-network/tools-key-gen-cli/commit/17e325f8b45bbbea6f6d0332a8c821b976eebbe8))
* Retry by updating hashes in requirements ([6eb67a9](https://github.com/lukso-network/tools-key-gen-cli/commit/6eb67a937977e7102081b80d2e1bab4dd27e3214))
* To get fat binary needs to install cytoolz no binary ([33a0a1a](https://github.com/lukso-network/tools-key-gen-cli/commit/33a0a1a261d87739c2b06013687f199846230ada))
* Upgrade macholib ([d3c46ac](https://github.com/lukso-network/tools-key-gen-cli/commit/d3c46ac8d96dce806ea0694be92f373826ba635d))
* Upgrade pefile ([6c6cc15](https://github.com/lukso-network/tools-key-gen-cli/commit/6c6cc15424e3c77eb41a541a8d8ac7260a3c83c2))
* Wrong place to apply -nocytoolz ([85c93c9](https://github.com/lukso-network/tools-key-gen-cli/commit/85c93c95bca80aeef113d04a9316201d840c4f07))

## [2.5.2](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.5.1...v2.5.2) (2023-04-13)


### Bug Fixes

* Remove unused networks (signed commit) ([a957cbc](https://github.com/lukso-network/tools-key-gen-cli/commit/a957cbcf3ce9d0ce5ce77ec2def561e01a8c0cb6))

## [2.5.1](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.5.0...v2.5.1) (2023-03-24)


### Bug Fixes

* . instead of slash ([7c9a0af](https://github.com/lukso-network/tools-key-gen-cli/commit/7c9a0afb9cdfbd51ed6f0b5197c299f548660613))
* Adjust some indirect dependencies ([979a1a1](https://github.com/lukso-network/tools-key-gen-cli/commit/979a1a1137d02e835219b1942b20827e20bce168))
* missing install keyword ([5d1ca50](https://github.com/lukso-network/tools-key-gen-cli/commit/5d1ca506c0ab76ae8a2c5fc7ee1878cbf64b7a4e))
* Network names. ([707924f](https://github.com/lukso-network/tools-key-gen-cli/commit/707924f4249debe17fbb551d3aef76180f9d714e))
* Remotely the bin folder cannot be used in pytemps. ([450c982](https://github.com/lukso-network/tools-key-gen-cli/commit/450c982ac40fb49bf6f37c968828c95da2bd30d8))
* Requirement path still wrong. ([a937dde](https://github.com/lukso-network/tools-key-gen-cli/commit/a937dde9248315f0ca72ee88491105e58f99261d))
* Restart migration to universal build. ([5997957](https://github.com/lukso-network/tools-key-gen-cli/commit/5997957798588fa59483782e0752321c43153e9a))

## [2.5.0](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.4.7...v2.5.0) (2023-03-13)


### Features

* added testnet and mainnet fork version ([e4c8298](https://github.com/lukso-network/tools-key-gen-cli/commit/e4c82987e1efd8c42430f09a2c8c3c14c9f5e611))

## [2.4.7](https://github.com/lukso-network/tools-key-gen-cli/compare/v2.4.6...v2.4.7) (2023-02-21)


### Bug Fixes

* Change repo name ([#18](https://github.com/lukso-network/tools-key-gen-cli/issues/18)) ([94507a6](https://github.com/lukso-network/tools-key-gen-cli/commit/94507a6bc84c0893d0dbb116b6948b3d7928946d))

## [2.4.6](https://github.com/lukso-network/tools-staking-deposit-cli/compare/v2.4.5...v2.4.6) (2023-01-27)


### Bug Fixes

* Genesis fork version should be 0x20220001 ([#16](https://github.com/lukso-network/tools-staking-deposit-cli/issues/16)) ([2f79b53](https://github.com/lukso-network/tools-staking-deposit-cli/commit/2f79b5325ba5a8fb30607e932b0363f644f9d2bc))

## [2.4.5](https://github.com/lukso-network/tools-staking-deposit-cli/compare/v2.4.4...v2.4.5) (2023-01-23)


### Bug Fixes

* Add default_factory around nested dataclasses ([e45099b](https://github.com/lukso-network/tools-staking-deposit-cli/commit/e45099ba1ba34249ac1d8e09aa3d82d4d239b668))

## [2.4.4](https://github.com/lukso-network/tools-staking-deposit-cli/compare/v2.4.3...v2.4.4) (2023-01-20)


### Bug Fixes

* Disable release-please process on pull_requests. It should only track things on push to develop or patch/* ([f52d510](https://github.com/lukso-network/tools-staking-deposit-cli/commit/f52d5109617dfb44c097606aa7bbc38a3cfda6ef))

## [2.4.3](https://github.com/lukso-network/tools-staking-deposit-cli/compare/v2.4.2...v2.4.3) (2022-12-13)


### Bug Fixes

* Use tags during submodule notify (the gui is expecting the input now) ([c98fc36](https://github.com/lukso-network/tools-staking-deposit-cli/commit/c98fc36afd6f1f71d127621967b464f027ca2881))

## [2.4.2](https://github.com/lukso-network/tools-staking-deposit-cli/compare/v2.4.1...v2.4.2) (2022-12-13)


### Bug Fixes

* Inherit secrets to allow notification ([903e8bd](https://github.com/lukso-network/tools-staking-deposit-cli/commit/903e8bdd2f7a73ef626aaa75e2af1a6dcd6f0297))

## [2.4.1](https://github.com/lukso-network/tools-staking-deposit-cli/compare/v2.4.0...v2.4.1) (2022-12-12)


### Bug Fixes

* Version import from the wrong file ([3b5f252](https://github.com/lukso-network/tools-staking-deposit-cli/commit/3b5f2529c0752e64c42c7a182816833a0f26745d))

## [2.4.0](https://github.com/lukso-network/tools-staking-deposit-cli/compare/v2.3.0...v2.4.0) (2022-12-02)


### Features

* Add LUKSO network support ([4b8acfe](https://github.com/lukso-network/tools-staking-deposit-cli/commit/4b8acfe099bdd8c1ebf04d15a9cbf3a1bdd53a2e))


### Bug Fixes

* Add release-please process ([cf57d55](https://github.com/lukso-network/tools-staking-deposit-cli/commit/cf57d559b7d9535f333b4fb74a53252f8ba7f371))
