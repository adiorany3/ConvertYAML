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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=214ms, nekobox=230ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-66MS` (url=206ms, nekobox=235ms, status=yes)
3. `AKUN-003-FMN5-RENTED-NET2-VLESS-WS-75MS` (url=217ms, nekobox=230ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-78MS` (url=207ms, nekobox=225ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=208ms, nekobox=228ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-84MS` (url=221ms, nekobox=191ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS`
8. `AKUN-007-GO-DADDY-COM-LLC-VLESS-WS-82MS`
9. `AKUN-008-POLICE-VLESS-WS-94MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS`
12. `AKUN-012-POLICE-VLESS-WS-103MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-116MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-75MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-98MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-103MS` (url=235ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-68MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-71MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-143MS` (url=211ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-135MS` (url=219ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-108MS` (url=327ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-117MS` (url=220ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-81MS` (url=211ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-111MS` (url=205ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
