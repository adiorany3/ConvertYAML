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
1. `AKUN-001-UNKNOWN-VLESS-WS-108MS` (url=693ms, nekobox=349ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-112MS` (url=319ms, nekobox=358ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-88MS` (url=294ms, nekobox=354ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-114MS` (url=331ms, nekobox=320ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=373ms, nekobox=336ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS` (url=354ms, nekobox=337ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-129MS` (url=322ms, nekobox=359ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-111MS` (url=289ms, nekobox=378ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=298ms, nekobox=344ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS` (url=287ms, nekobox=336ms, status=yes)
11. `AKUN-011-GO-DADDY-COM-LLC-VLESS-WS-125MS` (url=339ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=273ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-141MS` (url=314ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-148MS` (url=312ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-143MS` (url=322ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-149MS` (url=308ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-156MS` (url=336ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-146MS` (url=297ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-157MS` (url=306ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-303MS` (url=663ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-137MS` (url=379ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-336MS` (url=4795ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-315MS` (url=645ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-125MS` (url=343ms, status=HTTP 204)
25. `AKUN-025-MICROSOFT-VLESS-WS-351MS` (url=741ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
