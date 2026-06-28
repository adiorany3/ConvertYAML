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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=223ms, nekobox=280ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-111MS` (url=257ms, nekobox=264ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-113MS` (url=233ms, nekobox=252ms, status=yes)
4. `AKUN-004-MEDIUM-VLESS-WS-114MS` (url=228ms, nekobox=244ms, status=yes)
5. `AKUN-005-466688-VLESS-WS-126MS` (url=236ms, nekobox=342ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-105MS` (url=231ms, nekobox=245ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-126MS` (url=232ms, nekobox=275ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=212ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS` (url=214ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=210ms, nekobox=247ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-124MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-122MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-102MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-155MS` (url=264ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-145MS` (url=423ms, status=HTTP 204)
16. `AKUN-016-ADF-VLESS-WS-96MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-381MS` (url=757ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-364MS` (url=769ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-372MS` (url=790ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-404MS` (url=840ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-391MS` (url=900ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-391MS` (url=851ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-402MS` (url=834ms, status=HTTP 204)
24. `AKUN-024-DEV-VLESS-WS-563MS` (url=689ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-549MS` (url=653ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
