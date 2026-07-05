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
1. `AKUN-001-ALIBABA-VLESS-WS-64MS` (url=224ms, nekobox=243ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-69MS` (url=220ms, nekobox=246ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-61MS` (url=223ms, nekobox=254ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-60MS` (url=220ms, nekobox=240ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-69MS` (url=215ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS` (url=214ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-59MS` (url=217ms, nekobox=239ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=204ms, nekobox=327ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS` (url=221ms, nekobox=243ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=225ms, nekobox=248ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-81MS` (url=212ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-87MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-107MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-105MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-95MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-65MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-345MS` (url=788ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-377MS` (url=777ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-369MS` (url=827ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-386MS` (url=801ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-354MS` (url=757ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-379MS` (url=817ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-347MS` (url=728ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-385MS` (url=825ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-442MS` (url=4288ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
