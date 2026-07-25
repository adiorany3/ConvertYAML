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
1. `AKUN-001-UNKNOWN-VLESS-WS-78MS` (url=293ms, nekobox=386ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-77MS` (url=355ms, nekobox=372ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-77MS` (url=308ms, nekobox=345ms, status=yes)
4. `AKUN-004-SPEEDTEST-VLESS-WS-83MS` (url=269ms, nekobox=222ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-85MS`
6. `AKUN-005-3666888-VLESS-WS-95MS`
7. `AKUN-007-SPEEDTEST-VLESS-WS-99MS` (url=350ms, nekobox=207ms, status=no)
8. `AKUN-006-UNKNOWN-VLESS-WS-107MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-100MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-145MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-179MS`
13. `AKUN-013-SPEEDTEST-VLESS-WS-101MS` (url=304ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=406ms, status=HTTP 204)
15. `AKUN-015-LEVIKOGJGFDD-VLESS-WS-208MS` (url=376ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-208MS` (url=332ms, status=HTTP 204)
17. `AKUN-017-SPEEDTEST-VLESS-WS-125MS` (url=345ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-202MS` (url=416ms, status=HTTP 204)
19. `AKUN-019-LEVIKOGJGFDD-VLESS-WS-278MS` (url=572ms, status=HTTP 204)
20. `AKUN-020-SPEEDTEST-VLESS-WS-310MS` (url=743ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-112MS` (url=348ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-637MS` (url=1013ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-647MS` (url=1000ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-601MS` (url=1003ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-74MS` (url=275ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
