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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-182MS` (url=336ms, nekobox=364ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-185MS` (url=343ms, nekobox=402ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-183MS` (url=294ms, nekobox=347ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-182MS` (url=325ms, nekobox=360ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-185MS` (url=329ms, nekobox=354ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-186MS` (url=334ms, nekobox=357ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-186MS` (url=344ms, nekobox=355ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-189MS` (url=328ms, nekobox=351ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-189MS` (url=321ms, nekobox=364ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-184MS` (url=336ms, nekobox=403ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-191MS` (url=338ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-193MS` (url=342ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-184MS` (url=352ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-186MS` (url=347ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-198MS` (url=344ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-200MS` (url=340ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-194MS` (url=325ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-195MS` (url=361ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-183MS` (url=320ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-199MS` (url=407ms, status=HTTP 204)
21. `AKUN-021-MEDIUM-VLESS-WS-227MS` (url=304ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-216MS` (url=487ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-225MS` (url=362ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-218MS` (url=376ms, status=HTTP 204)
25. `AKUN-025-242311-VLESS-WS-219MS` (url=328ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
