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
1. `AKUN-001-ORACLE-VLESS-WS-63MS` (url=215ms, nekobox=246ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-62MS` (url=251ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=209ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=219ms, nekobox=227ms, status=yes)
5. `AKUN-005-DIXONS-VLESS-WS-101MS` (url=223ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=211ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-61MS` (url=222ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-101MS` (url=214ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=216ms, nekobox=248ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-116MS` (url=216ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-132MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-WPENG-VLESS-WS-122MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-112MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-100MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-137MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-108MS` (url=218ms, status=HTTP 204)
17. `AKUN-018-PAGES-VLESS-WS-100MS` (url=200ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-117MS` (url=214ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-112MS` (url=215ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-132MS` (url=243ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-72MS` (url=214ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-125MS` (url=204ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-74MS` (url=219ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-373MS` (url=811ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-387MS` (url=725ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
