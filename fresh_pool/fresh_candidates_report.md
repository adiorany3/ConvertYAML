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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-79MS` (url=226ms, nekobox=246ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-82MS` (url=199ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=227ms, nekobox=260ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=219ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=230ms, nekobox=236ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=232ms, nekobox=231ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-97MS` (url=207ms, nekobox=231ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=208ms, nekobox=264ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-100MS` (url=208ms, nekobox=7176ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS`
11. `AKUN-010-466688-VLESS-WS-95MS`
12. `AKUN-012-466688-VLESS-WS-100MS` (url=209ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-129MS` (url=254ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-114MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-PUBLICDOMAINREGISTRY-NET-VLESS-WS-111MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-HETZNER-VLESS-WS-116MS` (url=209ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-120MS` (url=237ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-137MS` (url=241ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-170MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-256MS` (url=520ms, status=HTTP 204)
21. `AKUN-021-INTERNETWORKS-45-131-210-VLESS-WS-254MS` (url=567ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-250MS` (url=514ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-265MS` (url=561ms, status=HTTP 204)
24. `AKUN-024-ILOVEZHENJIU-VLESS-WS-366MS` (url=700ms, status=HTTP 204)
25. `AKUN-025-DEV-VLESS-WS-90MS` (url=626ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
