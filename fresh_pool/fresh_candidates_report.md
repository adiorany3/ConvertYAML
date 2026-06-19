# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-ORACLE-VLESS-WS-64MS` (url=207ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=220ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=222ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-59MS` (url=214ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=210ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS` (url=209ms, nekobox=251ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=218ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=223ms, nekobox=180ms, status=no)
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-107MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-254MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-256MS` (url=593ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-265MS` (url=568ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-276MS` (url=4403ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-283MS` (url=555ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-282MS` (url=555ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-300MS` (url=5603ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-273MS` (url=2680ms, status=HTTP 204)
19. `AKUN-029-CLOUDFLARE-VLESS-WS-520MS` (url=5046ms, status=HTTP 204)
20. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-524MS` (url=1308ms, status=HTTP 204)
21. `AKUN-031-RS-RAPIDSEEDBOX-20190717-VLESS-WS-523MS` (url=1804ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
