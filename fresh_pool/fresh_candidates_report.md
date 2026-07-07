# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=255ms, nekobox=279ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-82MS` (url=250ms, nekobox=269ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-82MS` (url=245ms, nekobox=254ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=228ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=245ms, nekobox=274ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=244ms, nekobox=314ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=231ms, nekobox=269ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=236ms, nekobox=260ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS` (url=248ms, nekobox=258ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=246ms, nekobox=193ms, status=no)
11. `AKUN-010-WPENG-VLESS-WS-274MS`
12. `AKUN-014-LT-LRTC-20060503-VLESS-WS-277MS` (url=711ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-293MS` (url=637ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-283MS` (url=639ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-266MS` (url=579ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-302MS` (url=594ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-320MS` (url=415ms, status=HTTP 204)
18. `AKUN-022-UNKNOWN-VLESS-WS-459MS` (url=842ms, status=HTTP 204)
19. `AKUN-024-UNKNOWN-VLESS-WS-276MS` (url=554ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-523MS` (url=864ms, status=HTTP 204)
21. `AKUN-029-UNKNOWN-VLESS-WS-597MS` (url=992ms, status=HTTP 204)
22. `AKUN-032-UNKNOWN-VLESS-WS-296MS` (url=1582ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
