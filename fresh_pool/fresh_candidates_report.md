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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=196ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-60MS` (url=225ms, nekobox=226ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=197ms, nekobox=229ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-61MS` (url=200ms, nekobox=230ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-87MS` (url=201ms, nekobox=222ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS` (url=202ms, nekobox=237ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-87MS` (url=202ms, nekobox=230ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-62MS` (url=197ms, nekobox=225ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-70MS` (url=225ms, nekobox=245ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-99MS` (url=214ms, nekobox=242ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-76MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-102MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-84MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-DE-CLOUDKLEYER-20190515-VLESS-WS-138MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-107MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-157MS` (url=205ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-111MS` (url=227ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-108MS` (url=245ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-76MS` (url=354ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-395MS` (url=644ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-405MS` (url=921ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-424MS` (url=876ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-395MS` (url=730ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-442MS` (url=866ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-440MS` (url=719ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
