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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=207ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=213ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=210ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=228ms, nekobox=233ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-77MS` (url=231ms, nekobox=257ms, status=yes)
6. `AKUN-006-UK-GB-DCL-01-20191003-VLESS-WS-61MS` (url=223ms, nekobox=247ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-83MS` (url=207ms, nekobox=239ms, status=yes)
8. `AKUN-008-OVH-VLESS-WS-76MS` (url=204ms, nekobox=281ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-79MS` (url=208ms, nekobox=233ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-85MS` (url=212ms, nekobox=257ms, status=yes)
11. `AKUN-011-DIGITALOCEAN-VLESS-WS-84MS` (url=204ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-88MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-79MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-82MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-76MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-83MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-75MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-ADF-VLESS-WS-107MS` (url=200ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-92MS` (url=232ms, status=HTTP 204)
20. `AKUN-020-SPEEDTEST-VLESS-WS-89MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-90MS` (url=212ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-125MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-99MS` (url=201ms, status=HTTP 204)
24. `AKUN-024-MYBB-VLESS-WS-71MS` (url=226ms, status=HTTP 204)
25. `AKUN-025-WEBEX-VLESS-WS-94MS` (url=276ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
