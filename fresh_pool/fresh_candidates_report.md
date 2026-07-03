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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-76MS` (url=217ms, nekobox=231ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=220ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=203ms, nekobox=260ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-100MS` (url=241ms, nekobox=236ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-96MS` (url=231ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=230ms, nekobox=235ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-92MS` (url=236ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-115MS` (url=228ms, nekobox=236ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-93MS` (url=217ms, nekobox=239ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-98MS` (url=207ms, nekobox=238ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=268ms, status=HTTP 204)
12. `AKUN-012-SSL-1134-VLESS-WS-112MS` (url=259ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-84MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-95MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-97MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-WEBEX-VLESS-WS-89MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-104MS` (url=201ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-110MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-109MS` (url=238ms, status=HTTP 204)
20. `AKUN-020-COMPREND-NET-VLESS-WS-151MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-85MS` (url=230ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-110MS` (url=223ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-242MS` (url=532ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-249MS` (url=535ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-253MS` (url=564ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
