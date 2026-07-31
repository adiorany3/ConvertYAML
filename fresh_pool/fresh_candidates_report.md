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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=199ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=202ms, nekobox=225ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=210ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-60MS` (url=207ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-58MS` (url=207ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-60MS` (url=217ms, nekobox=172ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-65MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-89MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS`
10. `AKUN-009-MYBB-VLESS-WS-97MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-65MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-131MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-62MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-60MS` (url=198ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-78MS` (url=199ms, status=HTTP 204)
16. `AKUN-016-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-127MS` (url=1561ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-66MS` (url=264ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-68MS` (url=204ms, status=HTTP 204)
19. `AKUN-019-NET-141-11-202-0-23-VLESS-WS-225MS` (url=474ms, status=HTTP 204)
20. `AKUN-021-LEVIKOGJGFDD-VLESS-WS-155MS` (url=266ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-304MS` (url=715ms, status=HTTP 204)
22. `AKUN-025-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-432MS` (url=835ms, status=HTTP 204)
23. `AKUN-026-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-437MS` (url=1117ms, status=HTTP 204)
24. `AKUN-027-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-442MS` (url=980ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-447MS` (url=806ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
