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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-191MS` (url=331ms, nekobox=355ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-191MS` (url=335ms, nekobox=415ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-192MS` (url=314ms, nekobox=379ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-185MS` (url=384ms, nekobox=296ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-191MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-199MS` (url=368ms, nekobox=7179ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-197MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-186MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-191MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-183MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-182MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-200MS` (url=311ms, nekobox=267ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-201MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-222MS` (url=346ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-219MS` (url=354ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-210MS` (url=360ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-214MS` (url=370ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-208MS` (url=328ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-225MS` (url=382ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-240MS` (url=365ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-252MS` (url=444ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-220MS` (url=410ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-205MS` (url=346ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-275MS` (url=334ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-183MS` (url=336ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
