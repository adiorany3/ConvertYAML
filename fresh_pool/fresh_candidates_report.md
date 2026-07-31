# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=226ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=226ms, nekobox=239ms, status=yes)
3. `AKUN-003-877774-VLESS-WS-83MS` (url=221ms, nekobox=238ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS` (url=200ms, nekobox=248ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-82MS` (url=244ms, nekobox=255ms, status=yes)
6. `AKUN-006-PAGES-VLESS-WS-104MS` (url=202ms, nekobox=256ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-83MS` (url=207ms, nekobox=233ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-80MS` (url=1576ms, nekobox=1344ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=235ms, nekobox=203ms, status=no)
10. `AKUN-009-UNKNOWN-VLESS-WS-100MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-109MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-84MS` (url=229ms, status=HTTP 204)
13. `AKUN-014-RMGYVPN-VLESS-WS-247MS` (url=556ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-371MS` (url=791ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-367MS` (url=1302ms, status=HTTP 204)
16. `AKUN-020-SOSKEYNETS-VLESS-WS-544MS` (url=1270ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-621MS` (url=1021ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-667MS` (url=1024ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-724MS` (url=3342ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-750MS` (url=1190ms, status=HTTP 204)
21. `AKUN-033-UNKNOWN-VLESS-WS-450MS` (url=4179ms, status=HTTP 204)
22. `AKUN-034-CLOUDFLARE-VLESS-WS-652MS` (url=1067ms, status=HTTP 204)
23. `AKUN-035-CLOUDFLARE-VLESS-WS-797MS` (url=1333ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
