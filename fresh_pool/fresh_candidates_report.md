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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=219ms, nekobox=227ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-70MS` (url=198ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=223ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=214ms, nekobox=175ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-64MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS`
7. `AKUN-006-VULTR-VLESS-WS-65MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-66MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-82MS` (url=198ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-62MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-72MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-64MS` (url=201ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-75MS` (url=197ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-67MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-79MS` (url=215ms, status=HTTP 204)
19. `AKUN-020-MYBB-VLESS-WS-72MS` (url=217ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-78MS` (url=216ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-91MS` (url=195ms, status=HTTP 204)
22. `AKUN-023-LT-LRTC-20060503-VLESS-WS-212MS` (url=1728ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-224MS` (url=489ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-169MS` (url=239ms, status=HTTP 204)
25. `AKUN-026-SKK-VLESS-WS-320MS` (url=655ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
