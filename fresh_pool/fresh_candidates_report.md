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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-ZVC-VLESS-WS-75MS` (url=218ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=205ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS` (url=215ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-106MS` (url=206ms, nekobox=244ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-88MS` (url=223ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=204ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS` (url=224ms, nekobox=232ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-129MS` (url=227ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS` (url=237ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-134MS` (url=355ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-168MS` (url=271ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-215MS` (url=281ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-251MS` (url=544ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-252MS` (url=1707ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-291MS` (url=3718ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-272MS` (url=543ms, status=HTTP 204)
18. `AKUN-022-UNKNOWN-VLESS-WS-285MS` (url=581ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-437MS` (url=725ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-410MS` (url=701ms, status=HTTP 204)
21. `AKUN-027-HOSTES-LLC-VLESS-WS-514MS` (url=838ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-512MS` (url=854ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-587MS` (url=1550ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-772MS` (url=1641ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-775MS` (url=1679ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
