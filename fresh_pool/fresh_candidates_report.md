# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-UNKNOWN-VLESS-WS-91MS` (url=235ms, nekobox=261ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-113MS` (url=235ms, nekobox=294ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-101MS` (url=243ms, nekobox=307ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-126MS` (url=242ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-101MS` (url=252ms, nekobox=254ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=252ms, nekobox=234ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS` (url=207ms, nekobox=250ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-117MS` (url=256ms, nekobox=239ms, status=yes)
9. `AKUN-009-UK-GB-DCL-01-20191003-VLESS-WS-130MS` (url=253ms, nekobox=245ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-195MS` (url=253ms, nekobox=253ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-109MS` (url=275ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-363MS` (url=636ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-385MS` (url=781ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-407MS` (url=797ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-411MS` (url=842ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-396MS` (url=851ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-418MS` (url=867ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-435MS` (url=847ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-436MS` (url=845ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-436MS` (url=915ms, status=HTTP 204)
21. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-726MS` (url=1265ms, status=HTTP 204)
22. `AKUN-028-CCTVHIKVISION-VLESS-WS-772MS` (url=1071ms, status=HTTP 204)
23. `AKUN-029-RC-PRO-5-VLESS-WS-770MS` (url=1235ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-711MS` (url=1538ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
