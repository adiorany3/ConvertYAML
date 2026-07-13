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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-90MS` (url=213ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=226ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-101MS` (url=251ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=233ms, nekobox=258ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=221ms, nekobox=281ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS` (url=230ms, nekobox=233ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=232ms, nekobox=259ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-143MS` (url=215ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS` (url=213ms, nekobox=300ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-132MS` (url=229ms, nekobox=247ms, status=yes)
11. `AKUN-011-PUBLICDOMAINREGISTRY-NET-VLESS-WS-149MS` (url=267ms, status=HTTP 204)
12. `AKUN-012-1PASSWORD-VLESS-WS-94MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-ZOOM-VLESS-WS-135MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UDACITY-VLESS-WS-146MS` (url=260ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-165MS` (url=291ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-146MS` (url=240ms, status=HTTP 204)
17. `AKUN-017-SHOPIFY-VLESS-WS-112MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-ADF-VLESS-WS-238MS` (url=219ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-128MS` (url=257ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-130MS` (url=369ms, status=HTTP 204)
21. `AKUN-021-US-VLESS-WS-159MS` (url=240ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-153MS` (url=322ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-155MS` (url=216ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-371MS` (url=825ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-369MS` (url=759ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
