# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-UNKNOWN-VLESS-WS-137MS` (url=320ms, nekobox=299ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-138MS` (url=292ms, nekobox=311ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-131MS` (url=292ms, nekobox=307ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-137MS` (url=264ms, nekobox=315ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-134MS` (url=326ms, nekobox=292ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-147MS` (url=259ms, nekobox=292ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-148MS` (url=275ms, nekobox=293ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-151MS` (url=268ms, nekobox=307ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-152MS` (url=269ms, nekobox=304ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-157MS` (url=261ms, nekobox=298ms, status=yes)
11. `AKUN-012-PAGES-VLESS-WS-175MS` (url=293ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-273MS` (url=495ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-427MS` (url=2486ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-620MS` (url=1045ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-647MS` (url=965ms, status=HTTP 204)
16. `AKUN-019-SUKARIO-VLESS-WS-594MS` (url=941ms, status=HTTP 204)
17. `AKUN-023-UNKNOWN-VLESS-WS-684MS` (url=1168ms, status=HTTP 204)
18. `AKUN-026-UNKNOWN-VLESS-WS-768MS` (url=3234ms, status=HTTP 204)
19. `AKUN-030-CLOUDFLARE-VLESS-WS-726MS` (url=1244ms, status=HTTP 204)
20. `AKUN-032-UNKNOWN-VLESS-WS-765MS` (url=4051ms, status=HTTP 204)
21. `AKUN-033-CLOUDFLARE-VLESS-WS-792MS` (url=1092ms, status=HTTP 204)
22. `AKUN-034-CLOUDFLARE-VLESS-WS-663MS` (url=1068ms, status=HTTP 204)
23. `AKUN-035-CLOUDFLARE-VLESS-WS-764MS` (url=1140ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
