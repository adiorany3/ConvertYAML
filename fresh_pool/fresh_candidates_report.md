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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=212ms, nekobox=237ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-91MS` (url=274ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=243ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=220ms, nekobox=261ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=234ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=218ms, nekobox=253ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=220ms, nekobox=255ms, status=yes)
9. `AKUN-009-WEYRO-NET-VLESS-WS-113MS` (url=229ms, nekobox=250ms, status=yes)
10. `AKUN-010-OVH-VLESS-WS-111MS` (url=213ms, nekobox=252ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-95MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-81MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-102MS` (url=357ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-112MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-115MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-PAGES-VLESS-WS-101MS` (url=210ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-238MS` (url=524ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-256MS` (url=516ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-251MS` (url=553ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-261MS` (url=558ms, status=HTTP 204)
21. `AKUN-023-SPEEDTEST-VLESS-WS-251MS` (url=501ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-261MS` (url=576ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-281MS` (url=560ms, status=HTTP 204)
24. `AKUN-026-466688-VLESS-WS-270MS` (url=385ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-372MS` (url=501ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
