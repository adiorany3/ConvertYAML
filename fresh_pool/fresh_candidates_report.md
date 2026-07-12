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
1. `AKUN-001-UNKNOWN-VLESS-WS-126MS` (url=298ms, nekobox=306ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-142MS` (url=279ms, nekobox=300ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-147MS` (url=357ms, nekobox=325ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-138MS` (url=279ms, nekobox=301ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-144MS` (url=283ms, nekobox=318ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-146MS` (url=298ms, nekobox=322ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-154MS` (url=301ms, nekobox=320ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS` (url=281ms, nekobox=294ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-146MS` (url=273ms, nekobox=302ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-139MS` (url=246ms, nekobox=240ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-148MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-138MS` (url=410ms, status=HTTP 204)
13. `AKUN-013-NET-82-21-84-0-24-VLESS-WS-130MS` (url=297ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-162MS` (url=250ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-128MS` (url=295ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-156MS` (url=243ms, status=HTTP 204)
17. `AKUN-017-PUBLICDOMAINREGISTRY-NET-VLESS-WS-170MS` (url=316ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-150MS` (url=289ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-182MS` (url=446ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-177MS` (url=263ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-140MS` (url=285ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-138MS` (url=276ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-153MS` (url=287ms, status=HTTP 204)
24. `AKUN-024-SHOPIFY-VLESS-WS-143MS` (url=292ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-180MS` (url=368ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
