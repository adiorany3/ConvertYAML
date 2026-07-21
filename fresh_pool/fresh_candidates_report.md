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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-110MS` (url=272ms, nekobox=315ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-110MS` (url=280ms, nekobox=345ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-116MS` (url=322ms, nekobox=320ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-128MS` (url=351ms, nekobox=312ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-128MS` (url=283ms, nekobox=346ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS` (url=299ms, nekobox=329ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-135MS` (url=299ms, nekobox=308ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-146MS` (url=311ms, nekobox=337ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-143MS` (url=313ms, nekobox=317ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-118MS` (url=284ms, nekobox=342ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-137MS` (url=407ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-150MS` (url=304ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-155MS` (url=340ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-166MS` (url=300ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-175MS` (url=279ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-146MS` (url=326ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-157MS` (url=287ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-164MS` (url=358ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-135MS` (url=292ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-136MS` (url=317ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-280MS` (url=601ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-328MS` (url=666ms, status=HTTP 204)
23. `AKUN-024-SUKARIO-VLESS-WS-524MS` (url=858ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-536MS` (url=1191ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-529MS` (url=873ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
