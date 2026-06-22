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
1. `AKUN-001-UNKNOWN-VLESS-WS-69MS` (url=210ms, nekobox=286ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=210ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDWEBMANAGE-EU-FR-VLESS-WS-72MS` (url=231ms, nekobox=255ms, status=yes)
4. `AKUN-004-U1HOST-FRA-VLESS-WS-76MS` (url=221ms, nekobox=249ms, status=yes)
5. `AKUN-005-SPACECORE-VLESS-WS-69MS` (url=222ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-66MS` (url=206ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=228ms, nekobox=250ms, status=yes)
8. `AKUN-008-HOSTOFF-NET-VLESS-WS-84MS` (url=238ms, nekobox=249ms, status=yes)
9. `AKUN-009-NET-NL-VLESS-WS-75MS` (url=232ms, nekobox=237ms, status=yes)
10. `AKUN-010-NETCUP-VLESS-WS-71MS` (url=232ms, nekobox=266ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-MYBB-VLESS-WS-94MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-MEDIUM-VLESS-WS-77MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-96MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-74MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-107MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-99MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=209ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-93MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-ADF-VLESS-WS-106MS` (url=234ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-352MS` (url=764ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-335MS` (url=763ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-354MS` (url=769ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-385MS` (url=843ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
