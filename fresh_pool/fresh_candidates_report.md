# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-ORACLE-VLESS-WS-108MS` (url=230ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-94MS` (url=277ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-102MS` (url=252ms, nekobox=250ms, status=yes)
4. `AKUN-004-NODEJS-VLESS-WS-106MS` (url=211ms, nekobox=197ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-107MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-125MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-131MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-130MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-142MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-160MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-256MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-280MS` (url=566ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-270MS` (url=585ms, status=HTTP 204)
14. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-257MS` (url=578ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-296MS` (url=610ms, status=HTTP 204)
16. `AKUN-024-UNKNOWN-VLESS-WS-439MS` (url=744ms, status=HTTP 204)
17. `AKUN-027-KAWAII520-VLESS-WS-462MS` (url=719ms, status=HTTP 204)
18. `AKUN-028-UNKNOWN-VLESS-WS-304MS` (url=507ms, status=HTTP 204)
19. `AKUN-030-UNKNOWN-VLESS-WS-475MS` (url=671ms, status=HTTP 204)
20. `AKUN-033-RS-RAPIDSEEDBOX-20190717-VLESS-WS-512MS` (url=814ms, status=HTTP 204)
21. `AKUN-034-CLOUDFLARE-VLESS-WS-290MS` (url=557ms, status=HTTP 204)
22. `AKUN-035-UNKNOWN-VLESS-WS-382MS` (url=656ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
