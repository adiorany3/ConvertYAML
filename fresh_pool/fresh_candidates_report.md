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
1. `AKUN-001-UNKNOWN-VLESS-WS-72MS` (url=215ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=221ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=213ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=217ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=216ms, nekobox=245ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=221ms, nekobox=232ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=221ms, nekobox=253ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-85MS` (url=223ms, nekobox=228ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-85MS` (url=227ms, nekobox=252ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-83MS` (url=228ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=1088ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-89MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-72MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-74MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-83MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-73MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=212ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-89MS` (url=213ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-83MS` (url=232ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-152MS` (url=252ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-220MS` (url=500ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-229MS` (url=3522ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-249MS` (url=513ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
