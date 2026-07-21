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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-133MS` (url=273ms, nekobox=320ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-137MS` (url=284ms, nekobox=308ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-143MS` (url=265ms, nekobox=304ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-132MS` (url=271ms, nekobox=302ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-143MS` (url=272ms, nekobox=318ms, status=yes)
6. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS` (url=280ms, nekobox=232ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-146MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-146MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-156MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-153MS` (url=298ms, nekobox=252ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-146MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-157MS` (url=279ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-153MS` (url=263ms, status=HTTP 204)
15. `AKUN-016-ZVC-VLESS-WS-160MS` (url=294ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-134MS` (url=257ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-138MS` (url=274ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-171MS` (url=318ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-214MS` (url=335ms, status=HTTP 204)
20. `AKUN-022-ZVC-VLESS-WS-152MS` (url=331ms, status=HTTP 204)
21. `AKUN-023-WPENG-VLESS-WS-149MS` (url=301ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-265MS` (url=445ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-246MS` (url=289ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-358MS` (url=761ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-378MS` (url=783ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
