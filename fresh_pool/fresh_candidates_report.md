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
1. `AKUN-001-ZVC-VLESS-WS-62MS` (url=231ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=220ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=222ms, nekobox=7178ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-66MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-82MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-68MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-82MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-77MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-62MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-84MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-89MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-117MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-94MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-121MS` (url=276ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-133MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-144MS` (url=296ms, status=HTTP 204)
24. `AKUN-024-CCWU-VLESS-WS-69MS` (url=221ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-90MS` (url=207ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
