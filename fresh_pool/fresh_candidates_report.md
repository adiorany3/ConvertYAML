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
1. `AKUN-001-ZVC-VLESS-WS-72MS` (url=200ms, nekobox=242ms, status=yes)
2. `AKUN-002-CL-173-242-112-0-20-VLESS-WS-83MS` (url=219ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=214ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-81MS` (url=220ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=210ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=218ms, nekobox=243ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-83MS` (url=223ms, nekobox=254ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=229ms, nekobox=248ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-93MS` (url=234ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=219ms, nekobox=254ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-103MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-116MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-121MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-133MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-87MS` (url=233ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-113MS` (url=231ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-121MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-150MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-107MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-153MS` (url=266ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-130MS` (url=238ms, status=HTTP 204)
24. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-130MS` (url=231ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-230MS` (url=491ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
