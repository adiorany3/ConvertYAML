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
1. `AKUN-001-GOV-VLESS-WS-79MS` (url=294ms, nekobox=336ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-77MS` (url=292ms, nekobox=351ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=453ms, nekobox=393ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=372ms, nekobox=304ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=287ms, nekobox=408ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=360ms, nekobox=304ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-103MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-90MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=344ms, status=HTTP 204)
12. `AKUN-013-ZVC-VLESS-WS-126MS` (url=382ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-85MS` (url=342ms, status=HTTP 204)
14. `AKUN-015-WPENG-VLESS-WS-82MS` (url=356ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-119MS` (url=351ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-125MS` (url=326ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-124MS` (url=331ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-166MS` (url=338ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-161MS` (url=342ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-200MS` (url=429ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-195MS` (url=396ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-158MS` (url=369ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-297MS` (url=588ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-300MS` (url=605ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-304MS` (url=680ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
