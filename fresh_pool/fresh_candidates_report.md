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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=213ms, nekobox=254ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=201ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-79MS` (url=207ms, nekobox=230ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-81MS` (url=222ms, nekobox=259ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-89MS` (url=227ms, nekobox=191ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS`
9. `AKUN-008-COMPREND-NET-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-114MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-71MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-82MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-106MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-104MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-100MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-112MS` (url=211ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-91MS` (url=221ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-224MS` (url=494ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-78MS` (url=213ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-71MS` (url=230ms, status=HTTP 204)
24. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-243MS` (url=588ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-256MS` (url=545ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
