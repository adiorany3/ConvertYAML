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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=217ms, nekobox=246ms, status=yes)
2. `AKUN-002-SIN-VLESS-WS-61MS` (url=222ms, nekobox=248ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-78MS` (url=227ms, nekobox=236ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-67MS` (url=222ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-69MS` (url=221ms, nekobox=270ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-81MS` (url=215ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS` (url=228ms, nekobox=226ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-67MS` (url=213ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-68MS` (url=196ms, nekobox=249ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-108MS` (url=200ms, nekobox=273ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-72MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-142MS` (url=196ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=447ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-343MS` (url=744ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-359MS` (url=720ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-339MS` (url=803ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-383MS` (url=834ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-369MS` (url=857ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-394MS` (url=855ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-410MS` (url=841ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-345MS` (url=587ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-485MS` (url=882ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-673MS` (url=1138ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-726MS` (url=1298ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-804MS` (url=1322ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
