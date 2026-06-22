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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-138MS` (url=249ms, nekobox=310ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-135MS` (url=266ms, nekobox=292ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-142MS` (url=260ms, nekobox=316ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-142MS` (url=273ms, nekobox=293ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-148MS` (url=276ms, nekobox=301ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-151MS` (url=272ms, nekobox=305ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-146MS` (url=264ms, nekobox=247ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-147MS`
11. `AKUN-010-MEDIUM-VLESS-WS-137MS`
12. `AKUN-012-MYBB-VLESS-WS-154MS` (url=245ms, status=HTTP 204)
13. `AKUN-013-008500-VLESS-WS-163MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-154MS` (url=252ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-175MS` (url=278ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-144MS` (url=279ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-170MS` (url=267ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-155MS` (url=265ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-150MS` (url=267ms, status=HTTP 204)
20. `AKUN-020-OPENAI-VLESS-WS-201MS` (url=271ms, status=HTTP 204)
21. `AKUN-021-US-VLESS-WS-142MS` (url=271ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-189MS` (url=276ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-362MS` (url=682ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-348MS` (url=703ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-353MS` (url=688ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
