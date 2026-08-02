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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=213ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=218ms, nekobox=237ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=222ms, nekobox=170ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-82MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-60MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-87MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-102MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-102MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-147MS` (url=311ms, status=HTTP 204)
15. `AKUN-016-EE-WELCOMEHOST-20190515-VLESS-WS-137MS` (url=281ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-497MS` (url=1117ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-565MS` (url=1001ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-606MS` (url=1030ms, status=HTTP 204)
19. `AKUN-026-CLOUDFLARE-VLESS-WS-641MS` (url=1033ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-736MS` (url=2776ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-677MS` (url=1088ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-744MS` (url=1611ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-804MS` (url=1245ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-742MS` (url=1601ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-767MS` (url=1208ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
