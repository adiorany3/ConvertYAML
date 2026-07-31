# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=325ms, nekobox=306ms, status=yes)
2. `AKUN-002-IP-VLESS-WS-91MS` (url=291ms, nekobox=372ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-108MS` (url=424ms, nekobox=312ms, status=yes)
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-113MS` (url=280ms, nekobox=316ms, status=yes)
5. `AKUN-005-877774-VLESS-WS-119MS` (url=307ms, nekobox=320ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=260ms, nekobox=321ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-162MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-295MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-509MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-554MS`
11. `AKUN-013-UNKNOWN-VLESS-WS-559MS` (url=1003ms, status=HTTP 204)
12. `AKUN-014-UNKNOWN-VLESS-WS-558MS` (url=971ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-548MS` (url=1054ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-487MS` (url=904ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-568MS` (url=1295ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-592MS` (url=1619ms, status=HTTP 204)
17. `AKUN-020-UNKNOWN-VLESS-WS-558MS` (url=3953ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-594MS` (url=1025ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-550MS` (url=1068ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-564MS` (url=1043ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-579MS` (url=904ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-624MS` (url=627ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-656MS` (url=1612ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-223MS` (url=2485ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
