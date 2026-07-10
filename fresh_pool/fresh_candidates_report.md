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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-91MS` (url=330ms, nekobox=235ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=229ms, nekobox=233ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-95MS` (url=199ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=228ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=204ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=205ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=213ms, nekobox=246ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-105MS` (url=223ms, nekobox=232ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-123MS` (url=226ms, nekobox=268ms, status=yes)
10. `AKUN-010-ADF-VLESS-WS-125MS` (url=202ms, nekobox=264ms, status=yes)
11. `AKUN-011-NODEHOST-VLESS-WS-110MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-ES-FORNEX-20160629-VLESS-WS-122MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-107MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-116MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-177MS` (url=244ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-181MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-98MS` (url=219ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=245ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-200MS` (url=608ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-371MS` (url=807ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-378MS` (url=828ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-383MS` (url=974ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-398MS` (url=852ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
