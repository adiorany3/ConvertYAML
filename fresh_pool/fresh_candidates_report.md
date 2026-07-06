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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=223ms, nekobox=253ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-82MS` (url=262ms, nekobox=253ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-89MS` (url=213ms, nekobox=256ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-82MS` (url=225ms, nekobox=257ms, status=yes)
5. `AKUN-005-IBCS-DE-VLESS-WS-106MS` (url=230ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=218ms, nekobox=284ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=218ms, nekobox=243ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-133MS` (url=260ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=218ms, nekobox=254ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS` (url=224ms, nekobox=244ms, status=yes)
11. `AKUN-011-PAGES-VLESS-WS-159MS` (url=230ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-124MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-129MS` (url=268ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-84MS` (url=275ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-251MS` (url=573ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-254MS` (url=529ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-259MS` (url=538ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-285MS` (url=591ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-264MS` (url=688ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-303MS` (url=631ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-287MS` (url=611ms, status=HTTP 204)
22. `AKUN-022-CELESTARA-VLESS-WS-300MS` (url=610ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-89MS` (url=230ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-470MS` (url=770ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-462MS` (url=786ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
