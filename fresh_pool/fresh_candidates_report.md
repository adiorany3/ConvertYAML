# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

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
1. `AKUN-001-LEVIKOGJGFDD-VLESS-WS-74MS` (url=220ms, nekobox=265ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-84MS` (url=1549ms, nekobox=1638ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=213ms, nekobox=225ms, status=yes)
4. `AKUN-004-877774-VLESS-WS-80MS` (url=223ms, nekobox=232ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-83MS` (url=199ms, nekobox=234ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-96MS` (url=1231ms, nekobox=1748ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-98MS` (url=208ms, nekobox=249ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-76MS` (url=225ms, nekobox=260ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-123MS` (url=231ms, nekobox=271ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-135MS` (url=212ms, nekobox=258ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-102MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-PAGES-VLESS-WS-122MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=211ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-362MS` (url=732ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-359MS` (url=728ms, status=HTTP 204)
16. `AKUN-018-LEVIKOGJGFDD-VLESS-WS-364MS` (url=3594ms, status=HTTP 204)
17. `AKUN-022-TW-CLOUD-VLESS-WS-417MS` (url=1902ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-462MS` (url=997ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-625MS` (url=1045ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-780MS` (url=1328ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
