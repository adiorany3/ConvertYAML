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
1. `AKUN-001-CELESTARA-VLESS-WS-66MS` (url=212ms, nekobox=256ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-60MS` (url=209ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=196ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-64MS` (url=208ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS` (url=226ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS` (url=206ms, nekobox=227ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-70MS` (url=216ms, nekobox=268ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=225ms, nekobox=227ms, status=yes)
9. `AKUN-009-PUBLICDOMAINREGISTRY-NET-VLESS-WS-96MS` (url=213ms, nekobox=234ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-91MS` (url=207ms, nekobox=224ms, status=yes)
11. `AKUN-011-OVH-VLESS-WS-101MS` (url=206ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-PAGES-VLESS-WS-106MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-96MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-NODEJS-VLESS-WS-124MS` (url=196ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-139MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-122MS` (url=234ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-230MS` (url=481ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-229MS` (url=491ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-232MS` (url=575ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-255MS` (url=549ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-263MS` (url=555ms, status=HTTP 204)
23. `AKUN-031-PERSIANSHIELD-VLESS-WS-456MS` (url=724ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-494MS` (url=793ms, status=HTTP 204)
25. `AKUN-033-UNKNOWN-VLESS-WS-582MS` (url=721ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
