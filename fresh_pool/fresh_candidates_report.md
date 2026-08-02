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
1. `AKUN-001-UNKNOWN-VLESS-WS-56MS` (url=219ms, nekobox=234ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-54MS` (url=215ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-56MS` (url=211ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=211ms, nekobox=184ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-57MS` (url=222ms, nekobox=170ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-61MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS` (url=224ms, nekobox=172ms, status=no)
9. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-85MS` (url=217ms, nekobox=7178ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-64MS` (url=230ms, nekobox=171ms, status=no)
12. `AKUN-007-CLOUDFLARE-VLESS-WS-124MS`
13. `AKUN-008-DEV-VLESS-WS-121MS`
14. `AKUN-009-FASTVPSUS-IPV4-VLESS-WS-141MS`
15. `AKUN-010-CLOUDFLARE-VLESS-WS-157MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-73MS` (url=228ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-281MS` (url=583ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-332MS` (url=941ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-497MS` (url=1000ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-497MS` (url=973ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-516MS` (url=998ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-641MS` (url=1045ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-651MS` (url=1099ms, status=HTTP 204)
24. `AKUN-026-SUKARIO-VLESS-WS-594MS` (url=1053ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-621MS` (url=669ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
