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
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=217ms, nekobox=258ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-82MS` (url=208ms, nekobox=268ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-86MS` (url=200ms, nekobox=244ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-85MS` (url=227ms, nekobox=242ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-93MS` (url=225ms, nekobox=7178ms, status=no)
6. `AKUN-005-UNKNOWN-VLESS-WS-88MS`
7. `AKUN-006-MEDIUM-VLESS-WS-91MS`
8. `AKUN-007-ZOOM-VLESS-WS-82MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-84MS`
10. `AKUN-009-CCWU-VLESS-WS-119MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-94MS`
12. `AKUN-012-DEV-VLESS-WS-122MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=200ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-107MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-82MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-109MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-104MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-108MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS` (url=253ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-143MS` (url=229ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-127MS` (url=203ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-114MS` (url=215ms, status=HTTP 204)
24. `AKUN-024-1PASSWORD-VLESS-WS-123MS` (url=215ms, status=HTTP 204)
25. `AKUN-025-MYBB-VLESS-WS-84MS` (url=215ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
