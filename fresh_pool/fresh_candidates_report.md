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
1. `AKUN-001-MVPS-NET-VLESS-WS-80MS` (url=221ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=222ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=226ms, nekobox=252ms, status=yes)
4. `AKUN-004-EU-VLESS-WS-87MS` (url=212ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=232ms, nekobox=257ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-95MS` (url=227ms, nekobox=256ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-78MS` (url=219ms, nekobox=245ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-108MS` (url=215ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=210ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=235ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-163MS` (url=312ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-90MS` (url=252ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=251ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-142MS` (url=362ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-162MS` (url=486ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-236MS` (url=512ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-183MS` (url=282ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-244MS` (url=3087ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-304MS` (url=596ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-327MS` (url=538ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-234MS` (url=762ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-410MS` (url=669ms, status=HTTP 204)
23. `AKUN-028-ULTAHOST-VLESS-WS-446MS` (url=719ms, status=HTTP 204)
24. `AKUN-029-SUKARIO-VLESS-WS-435MS` (url=750ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-449MS` (url=761ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
