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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=222ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=222ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=211ms, nekobox=257ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS` (url=206ms, nekobox=243ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-100MS` (url=205ms, nekobox=226ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS` (url=213ms, nekobox=256ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=213ms, nekobox=260ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-73MS` (url=200ms, nekobox=253ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=207ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=278ms, nekobox=260ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-130MS` (url=245ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-96MS` (url=229ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-108MS` (url=210ms, status=HTTP 204)
14. `AKUN-017-UNKNOWN-VLESS-WS-244MS` (url=521ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-81MS` (url=245ms, status=HTTP 204)
16. `AKUN-019-UNKNOWN-VLESS-WS-248MS` (url=578ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=586ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-267MS` (url=498ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-254MS` (url=563ms, status=HTTP 204)
20. `AKUN-023-MICROSOFT-VLESS-WS-298MS` (url=586ms, status=HTTP 204)
21. `AKUN-024-COMPREND-NET-VLESS-WS-92MS` (url=204ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-406MS` (url=711ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-229MS` (url=509ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-786MS` (url=2597ms, status=HTTP 204)
25. `AKUN-035-RS-RAPIDSEEDBOX-20190717-VLESS-WS-774MS` (url=823ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
