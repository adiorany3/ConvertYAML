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
1. `AKUN-001-9889888-VLESS-WS-60MS` (url=221ms, nekobox=248ms, status=yes)
2. `AKUN-002-ADF-VLESS-WS-69MS` (url=209ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=211ms, nekobox=262ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-72MS` (url=229ms, nekobox=234ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-72MS` (url=230ms, nekobox=261ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, nekobox=251ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-60MS` (url=219ms, nekobox=250ms, status=yes)
8. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-75MS` (url=229ms, nekobox=262ms, status=yes)
9. `AKUN-009-DIXONS-VLESS-WS-109MS` (url=235ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=220ms, nekobox=289ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-108MS` (url=251ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-88MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-92MS` (url=207ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-97MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-77MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-95MS` (url=239ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-99MS` (url=235ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-98MS` (url=238ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-130MS` (url=230ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-141MS` (url=210ms, status=HTTP 204)
22. `AKUN-022-466688-VLESS-WS-161MS` (url=258ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-154MS` (url=363ms, status=HTTP 204)
24. `AKUN-024-SPEEDTEST-VLESS-WS-84MS` (url=242ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-104MS` (url=448ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
