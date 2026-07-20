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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=218ms, nekobox=261ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=227ms, nekobox=261ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-88MS` (url=212ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS` (url=206ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=204ms, nekobox=258ms, status=yes)
6. `AKUN-006-UK-GB-DCL-01-20191003-VLESS-WS-92MS` (url=206ms, nekobox=234ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-97MS` (url=228ms, nekobox=263ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-96MS` (url=225ms, nekobox=250ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-108MS` (url=200ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS` (url=268ms, nekobox=250ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-95MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-129MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-95MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-133MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-UK-GB-DCL-01-20191003-VLESS-WS-128MS` (url=245ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-131MS` (url=223ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-111MS` (url=237ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-149MS` (url=231ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-137MS` (url=233ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-134MS` (url=229ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-89MS` (url=201ms, status=HTTP 204)
25. `AKUN-025-LT-LRTC-20060503-VLESS-WS-243MS` (url=3735ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
