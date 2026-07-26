# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-ORACLE-VLESS-WS-72MS` (url=274ms, nekobox=330ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-71MS` (url=300ms, nekobox=356ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-75MS` (url=315ms, nekobox=347ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-82MS` (url=266ms, nekobox=7191ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-84MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-74MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-77MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-81MS`
9. `AKUN-008-DEV-VLESS-WS-83MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-86MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-94MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=271ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=273ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-109MS` (url=307ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-134MS` (url=376ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-150MS` (url=271ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-101MS` (url=281ms, status=HTTP 204)
18. `AKUN-018-008500-VLESS-WS-121MS` (url=309ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-110MS` (url=366ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-274MS` (url=779ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-79MS` (url=293ms, status=HTTP 204)
22. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-288MS` (url=4078ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-319MS` (url=869ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-328MS` (url=793ms, status=HTTP 204)
25. `AKUN-025-ZOOM-VLESS-WS-76MS` (url=321ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
