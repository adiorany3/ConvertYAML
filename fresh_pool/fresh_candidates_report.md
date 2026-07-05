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
1. `AKUN-001-OVH-VLESS-WS-56MS` (url=228ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, nekobox=240ms, status=yes)
3. `AKUN-003-CHSL-HEL-VLESS-WS-64MS` (url=227ms, nekobox=234ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS`
6. `AKUN-005-ZVC-VLESS-WS-68MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-65MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-89MS` (url=255ms, nekobox=204ms, status=no)
12. `AKUN-010-UNKNOWN-VLESS-WS-69MS`
13. `AKUN-013-WEBEX-VLESS-WS-73MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-96MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-WEBEX-VLESS-WS-70MS` (url=228ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-342MS` (url=781ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-384MS` (url=874ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-381MS` (url=793ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-371MS` (url=807ms, status=HTTP 204)
20. `AKUN-021-MICROSOFT-VLESS-WS-375MS` (url=798ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-375MS` (url=801ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-357MS` (url=749ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-672MS` (url=1086ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-682MS` (url=1148ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-704MS` (url=1093ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
